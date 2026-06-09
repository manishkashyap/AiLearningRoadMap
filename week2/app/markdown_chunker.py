import json
from pathlib import Path

chunk_size = 300  # words
chunk_overlap = 40  # words

PROJECT_DIR = Path(__file__).resolve().parents[2]
DOCUMENTS_DIR = PROJECT_DIR / "documents"
DATA_DIR = PROJECT_DIR / "week2" / "data"


def extract_topic_and_url(text: str) -> tuple[str, str]:
    topic = ""
    url = ""

    for line in text.splitlines():
        stripped_line = line.strip()

        if not topic and stripped_line:
            topic = stripped_line.removeprefix("#").strip()

        if stripped_line.startswith("- URL:"):
            url = stripped_line.removeprefix("- URL:").strip()

        if topic and url:
            break

    return topic, url


def split_text_into_word_chunks(
    filename: str,
    text: str,
    topic: str,
    url: str,
    document_dir: str,
) -> list[dict]:
    chunks = []
    words = text.split()

    for i in range(0, len(words), chunk_size - chunk_overlap):
        chunk_words = words[i : i + chunk_size]
        chunk_text = " ".join(chunk_words)

        chunks.append(
            {
                "chunk_id": f"{filename}::{i}",
                "source": filename,
                "document_dir": document_dir,
                "topic": topic,
                "url": url,
                "text": chunk_text,
            }
        )

    return chunks


def create_chunks_for_document_dir(dir_path: Path) -> int:
    all_chunks = []
    md_files = sorted(dir_path.glob("*.md"))

    if not md_files:
        print(f"No MD files found in {dir_path}.")
        return 0

    for file_path in md_files:
        print(file_path.name)

        text = file_path.read_text(encoding="utf-8")
        topic, url = extract_topic_and_url(text)
        text = text.strip(" \n")
        chunks = split_text_into_word_chunks(
            filename=file_path.name,
            text=text,
            topic=topic,
            url=url,
            document_dir=dir_path.name,
        )
        if chunks:
            all_chunks.extend(chunks)

    chunk_dir = DATA_DIR / dir_path.name
    chunk_dir.mkdir(parents=True, exist_ok=True)
    chunks_file = chunk_dir / "chunks.json"
    chunks_file.write_text(
        json.dumps(all_chunks, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"Saved {len(all_chunks)} chunks to {chunks_file}")
    return len(all_chunks)


def create_chunks_for_all_document_dirs() -> None:
    document_dirs = sorted(path for path in DOCUMENTS_DIR.iterdir() if path.is_dir())

    if not document_dirs:
        print(f"No document directories found in {DOCUMENTS_DIR}.")
        return

    total_chunks = 0
    for document_dir in document_dirs:
        print(f"\nProcessing {document_dir.name}")
        total_chunks += create_chunks_for_document_dir(document_dir)

    print(f"\nSaved {total_chunks} chunks across {len(document_dirs)} document directories.")


if __name__ == "__main__":
    create_chunks_for_all_document_dirs()
