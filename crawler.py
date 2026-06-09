#!/usr/bin/env python3
"""
Polite crawler for selected WebEngage documentation/resource URLs.

The crawler:
- checks robots.txt per domain before fetching a URL
- waits between sequential requests per domain
- applies exponential backoff for 429 and 503 responses
- limits crawl depth
- extracts page title, main text, publication date, and URL
- writes each collected page to its own Markdown file
"""

from __future__ import annotations

import argparse
import re
import time
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Iterable, Mapping
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup


START_URLS = {
    #"Dev Documentation" : "https://docs.webengage.com/",
    #"Blog" : "https://webengage.com/blog/",
    #"Knowledgebase" : "https://knowledgebase.webengage.com/",
    #"Product Releases" : "https://webengage.com/releases/",
    #"Case Studies" : "https://webengage.com/case-studies/",
    #"EBooks" : "https://webengage.com/resource/ebook/",
    "Glossary" : "https://webengage.com/resource/glossary/",
}
    


USER_AGENT = "CustomDataBot/1.0 (+https://example.com/contact)"
DEFAULT_CRAWL_DELAY_SECONDS = 1.0
DEFAULT_MAX_DEPTH = 10
DEFAULT_OUTPUT_DIR = "documents"
REQUEST_TIMEOUT_SECONDS = 5
BACKOFF_STATUSES = {429, 503}
MAX_RETRIES = 1


@dataclass(frozen=True)
class PageData:
    url: str
    title: str
    publication_date: str
    text: str


class PoliteCrawler:
    def __init__(
        self,
        start_urls: Iterable[str] | Mapping[str, str],
        output_dir: str,
        crawl_delay_seconds: float,
        max_depth: int,
        user_agent: str,
    ):
        if isinstance(start_urls, Mapping):
            start_urls = start_urls.values()

        self.start_urls = [normalize_url(url) for url in start_urls]
        self.output_dir = Path(output_dir)
        self.crawl_delay_seconds = crawl_delay_seconds
        self.max_depth = max_depth
        self.user_agent = user_agent
        self.allowed_domains = {urlparse(url).netloc for url in self.start_urls}
        self.allowed_prefixes = tuple(self.start_urls)

        self.session = requests.Session()
        self.session.headers.update({"User-Agent": self.user_agent})

        self.robot_parsers: dict[str, RobotFileParser] = {}
        self.last_request_at: dict[str, float] = {}

    def crawl(self) -> list[PageData]:
        queue = deque((url, 0) for url in self.start_urls)
        visited: set[str] = set()
        pages: list[PageData] = []

        while queue:
            url, depth = queue.popleft()

            if url in visited:
                continue

            if depth > self.max_depth:
                continue

            if not self.is_crawlable_url(url):
                continue

            if not self.allowed_by_robots(url):
                print(f"Skipping disallowed URL: {url}")
                visited.add(url)
                continue

            response = self.fetch(url)
            visited.add(url)

            if response is None:
                continue

            content_type = response.headers.get("content-type", "")
            if "text/html" not in content_type.lower():
                continue

            page_data, links = self.parse_page(response.url, response.text)

            if page_data.text:
                pages.append(page_data)
                print(f"Scraped: {page_data.url}")

            if depth == self.max_depth:
                continue

            for link in links:
                if link not in visited and self.is_crawlable_url(link):
                    queue.append((link, depth + 1))

        return pages

    def is_crawlable_url(self, url: str) -> bool:
        parsed = urlparse(url)

        if parsed.scheme not in {"http", "https"}:
            return False

        if parsed.netloc not in self.allowed_domains:
            return False

        return any(url.startswith(prefix) for prefix in self.allowed_prefixes)

    def allowed_by_robots(self, url: str) -> bool:
        parsed = urlparse(url)
        parser = self.get_robot_parser(parsed.scheme, parsed.netloc)
        return parser.can_fetch(self.user_agent, url)

    def get_robot_parser(self, scheme: str, netloc: str) -> RobotFileParser:
        if netloc in self.robot_parsers:
            return self.robot_parsers[netloc]

        robots_url = f"{scheme}://{netloc}/robots.txt"
        parser = RobotFileParser()
        parser.set_url(robots_url)

        try:
            self.wait_for_domain(netloc)
            response = self.session.get(robots_url, timeout=REQUEST_TIMEOUT_SECONDS)
            self.last_request_at[netloc] = time.monotonic()

            if response.status_code == 200:
                parser.parse(response.text.splitlines())
            else:
                print(f"robots.txt unavailable ({response.status_code}) for {netloc}; allowing crawl.")
                parser.parse([])
        except requests.RequestException as exc:
            print(f"robots.txt request failed for {netloc}: {exc}; allowing crawl.")
            parser.parse([])

        self.robot_parsers[netloc] = parser
        return parser

    def fetch(self, url: str) -> requests.Response | None:
        parsed = urlparse(url)
        delay = self.crawl_delay_seconds

        for attempt in range(MAX_RETRIES + 1):
            self.wait_for_domain(parsed.netloc, delay)

            try:
                response = self.session.get(url, timeout=REQUEST_TIMEOUT_SECONDS)
                self.last_request_at[parsed.netloc] = time.monotonic()
            except requests.RequestException as exc:
                print(f"Request failed for {url}: {exc}")
                return None

            if response.status_code in BACKOFF_STATUSES:
                retry_after = parse_retry_after(response.headers.get("retry-after"))
                sleep_for = retry_after if retry_after is not None else delay * (2**attempt)
                print(f"{response.status_code} for {url}; backing off for {sleep_for:.1f}s")
                time.sleep(sleep_for)
                delay = max(delay * 2, sleep_for)
                continue

            if response.status_code >= 400:
                print(f"Skipping {url}; HTTP {response.status_code}")
                return None

            return response

        print(f"Skipping {url}; exceeded retry limit")
        return None

    def wait_for_domain(self, netloc: str, delay: float | None = None) -> None:
        delay = self.crawl_delay_seconds if delay is None else delay
        last_request = self.last_request_at.get(netloc)

        if last_request is None:
            return

        elapsed = time.monotonic() - last_request
        remaining = delay - elapsed

        if remaining > 0:
            time.sleep(remaining)

    def parse_page(self, url: str, html: str) -> tuple[PageData, list[str]]:
        soup = BeautifulSoup(html, "html.parser")

        for tag in soup(["script", "style", "noscript", "svg"]):
            tag.decompose()

        title = extract_title(soup)
        publication_date = extract_publication_date(soup)
        text = extract_main_text(soup)
        links = extract_links(url, soup)

        return PageData(
            url=url,
            title=title,
            publication_date=publication_date,
            text=text,
        ), links

    def write_markdown_files(self, pages: list[PageData]) -> list[Path]:
        generated_at = datetime.now(timezone.utc).isoformat()
        self.output_dir.mkdir(parents=True, exist_ok=True)

        written_files: list[Path] = []
        used_filenames: set[str] = set()

        for page in pages:
            filename = unique_filename(page, used_filenames)
            output_path = self.output_dir / filename
            lines = [
                f"# {page.title or 'Untitled'}",
                "",
                f"- URL: {page.url}",
                f"- Publication Date: {page.publication_date or 'Not found'}",
                f"- Scraped At: {generated_at}",
                "",
                page.text,
                "",
            ]
            output_path.write_text("\n".join(lines), encoding="utf-8")
            written_files.append(output_path)

        return written_files


def normalize_url(url: str) -> str:
    url, _fragment = urldefrag(url)
    parsed = urlparse(url)

    if parsed.path and parsed.path != "/" and parsed.path.endswith("/"):
        parsed = parsed._replace(path=parsed.path.rstrip("/"))

    return parsed.geturl()


def parse_retry_after(value: str | None) -> float | None:
    if not value:
        return None

    if value.isdigit():
        return float(value)

    try:
        retry_at = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None

    return max(0.0, (retry_at - datetime.now(timezone.utc)).total_seconds())


def unique_filename(page: PageData, used_filenames: set[str]) -> str:
    parsed = urlparse(page.url)
    path_slug = slugify(f"{parsed.netloc} {parsed.path}")
    title_slug = slugify(page.title)

    base_name = path_slug or title_slug or "untitled"
    filename = f"{base_name}.md"
    counter = 2

    while filename in used_filenames:
        filename = f"{base_name}-{counter}.md"
        counter += 1

    used_filenames.add(filename)
    return filename


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"https?://", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value[:140]


def extract_title(soup: BeautifulSoup) -> str:
    meta_title = soup.find("meta", attrs={"property": "og:title"})
    if meta_title and meta_title.get("content"):
        return clean_text(meta_title["content"])

    h1 = soup.find("h1")
    if h1:
        return clean_text(h1.get_text(" ", strip=True))

    if soup.title:
        return clean_text(soup.title.get_text(" ", strip=True))

    return ""


def extract_publication_date(soup: BeautifulSoup) -> str:
    selectors = [
        ("meta", {"property": "article:published_time"}),
        ("meta", {"name": "date"}),
        ("meta", {"name": "publish-date"}),
        ("meta", {"name": "pubdate"}),
    ]

    for tag_name, attrs in selectors:
        tag = soup.find(tag_name, attrs=attrs)
        if tag and tag.get("content"):
            return clean_text(tag["content"])

    time_tag = soup.find("time")
    if time_tag:
        if time_tag.get("datetime"):
            return clean_text(time_tag["datetime"])
        return clean_text(time_tag.get_text(" ", strip=True))

    return ""


def extract_main_text(soup: BeautifulSoup) -> str:
    candidates = [
        soup.find("article"),
        soup.find("main"),
        soup.find(attrs={"role": "main"}),
        soup.body,
    ]

    for candidate in candidates:
        if not candidate:
            continue

        text = clean_text(candidate.get_text("\n", strip=True))
        if len(text) >= 200:
            return text

    return ""


def extract_links(base_url: str, soup: BeautifulSoup) -> list[str]:
    links: list[str] = []

    for anchor in soup.find_all("a", href=True):
        href = anchor["href"].strip()

        if not href or href.startswith(("mailto:", "tel:", "javascript:")):
            continue

        links.append(normalize_url(urljoin(base_url, href)))

    return links


def clean_text(text: str) -> str:
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Polite crawler for selected WebEngage URLs.")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="Directory for per-page Markdown files.")
    parser.add_argument("--delay", type=float, default=DEFAULT_CRAWL_DELAY_SECONDS, help="Seconds between requests per domain.")
    parser.add_argument("--max-depth", type=int, default=DEFAULT_MAX_DEPTH, help="Maximum crawl depth from seed URLs.")
    parser.add_argument("--user-agent", default=USER_AGENT, help="Custom crawler User-Agent header.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    crawler = PoliteCrawler(
        start_urls=START_URLS,
        output_dir=args.output_dir,
        crawl_delay_seconds=args.delay,
        max_depth=args.max_depth,
        user_agent=args.user_agent,
    )
    pages = crawler.crawl()
    written_files = crawler.write_markdown_files(pages)
    print(f"Saved {len(written_files)} Markdown files to {args.output_dir}")


if __name__ == "__main__":
    main()
