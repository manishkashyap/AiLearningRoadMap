import json
import os
from pathlib import Path
import argparse

import faiss
import numpy
import cohere
import re
from rank_bm25 import BM25Okapi

from embedder import embed_texts
from AnswerGenerator import RAGResult

PROJECT_DIR = Path(__file__).resolve().parents[2]
DOC_DIR = PROJECT_DIR / "documents"
DATA_DIR = PROJECT_DIR / "week2" / "data"
COHERE_RERANK_MODEL = "rerank-v4.0-fast"   # use v4.0-pro for max quality, fast for latency
DEFAULT_CANDIDATE_MULTIPLIER = 5
DEFAULT_CANDIDATE_COUNT = 50
BM25_NORMALIZED_MIN_SCORE = 0.35
RERANK_NORMALIZED_MIN_SCORE = 0.45
NO_RERANK_MIN_SCORE = 0.70
RERANK_MIN_SCORE = 0.60


def get_cohere_client():
    #api_key = os.environ.get("COHERE_API_KEY")
    #if not api_key:
    #    raise RuntimeError("Set COHERE_API_KEY before enabling Cohere reranking.")
    return cohere.ClientV2(api_key="5dC7jbU63Tf69Dr4EUEE4G58W9xzvo7OglimJ3vv")


def load_source_document(chunk: dict) -> str:
    file_path = DOC_DIR / chunk["document_dir"] / chunk["source"]

    if not file_path.exists():
        raise FileNotFoundError(f"Source document not found: {file_path}")

    return file_path.read_text(encoding="utf-8")

def build_rerank_document(chunk: dict, full_document_text: str) -> str:
    return f"""
    TOPIC: {chunk["topic"]}
    URL: {chunk["url"]}
    MATCHED CHUNK:
    {chunk["text"]}
    FULL DOCUMENT:
    {full_document_text}
    """

def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())

def bm25_text(item: dict) -> str:
    return f"""
    {item["document_dir"]}
    {item["topic"]}
    {item["url"]}
    {item["source"]}
    {item["text"]}
    """

def get_bm25_scores_for_candidates(query: str, chunks: list[dict]) -> None:
    corpus = [tokenize(bm25_text(chunk)) for chunk in chunks]
    bm25 = BM25Okapi(corpus)

    query_tokens = tokenize(query)
    scores = bm25.get_scores(query_tokens)

    for chunk, score in zip(chunks, scores):
        chunk["bm25_score"] = float(score)

    normalize_scores(chunks, "bm25_score")

def find_faiss_candidates(
    query: str,
    candidate_count: int,
) -> tuple[list[dict], list[dict]]:
    query_embedding = embed_texts([query]).astype("float32")
    chunks = []
    all_metadata = []

    category_dirs = sorted(
        path.parent
        for path in DATA_DIR.glob("*/embeddings.npy")
        if (path.parent / "metadata.json").exists()
    )

    if not category_dirs:
        raise FileNotFoundError(f"No category indexes found in {DATA_DIR}.")

    for category_dir in category_dirs:
        embeddings = numpy.load(category_dir / "embeddings.npy").astype("float32")
        metadata = json.loads(
            (category_dir / "metadata.json").read_text(encoding="utf-8")
        )

        if len(metadata) != len(embeddings):
            raise ValueError(
                f"Index size mismatch in {category_dir}: "
                f"{len(metadata)} metadata records and {len(embeddings)} embeddings."
            )

        all_metadata.extend(metadata)
        category_candidate_count = min(candidate_count, len(metadata))

        index = faiss.IndexFlatIP(embeddings.shape[1])
        index.add(embeddings)
        distances, ranked_indices = index.search(
            query_embedding,
            k=category_candidate_count,
        )

        for distance, idx in zip(distances[0], ranked_indices[0]):
            item = metadata[int(idx)]
            chunks.append({
                "score": float(distance),
                "bm25_score": 0.0,
                "rerank_score": 0.0,
                "metadata_boost": 0.0,
                "final_score": 0.0,
                "chunk_id": item["chunk_id"],
                "topic": item["topic"],
                "url": item["url"],
                "source": item["source"],
                "document_dir": item.get("document_dir", category_dir.name),
                "text": item["text"],
            })

        print(
            f"Found {category_candidate_count} FAISS candidates "
            f"from {category_dir.name}"
        )

    normalize_scores(chunks, "score")
    return chunks, all_metadata

def normalize_scores(chunks: list[dict], key: str) -> None:
    values = [chunk[key] for chunk in chunks]
    max_value = max(values) if values else 0

    for chunk in chunks:
        chunk[f"{key}_normalized"] = chunk[key] / max_value if max_value else 0.0

def dedupe_by_source(chunks: list[dict]) -> list[dict]:
    best_by_source = {}

    for chunk in chunks:
        source_key = (chunk["document_dir"], chunk["source"])
        existing = best_by_source.get(source_key)

        if existing is None or chunk["final_score"] > existing["final_score"]:
            best_by_source[source_key] = chunk

    return list(best_by_source.values())

def get_chunk_offset(chunk_id: str) -> int:
    try:
        return int(chunk_id.split("::")[-1])
    except ValueError:
        return 0

def get_neighboring_chunks(
    matched_chunk: dict,
    metadata: list[dict],
    window: int = 1,
) -> list[dict]:
    source_chunks = [
        item
        for item in metadata
        if item["source"] == matched_chunk["source"]
        and item.get("document_dir") == matched_chunk.get("document_dir")
    ]
    source_chunks.sort(key=lambda item: get_chunk_offset(item["chunk_id"]))

    matched_index = None
    for index, item in enumerate(source_chunks):
        if item["chunk_id"] == matched_chunk["chunk_id"]:
            matched_index = index
            break

    if matched_index is None:
        return []

    start = max(0, matched_index - window)
    end = min(len(source_chunks), matched_index + window + 1)
    return source_chunks[start:end]

def attach_neighboring_chunks(
    chunks: list[dict],
    metadata: list[dict],
    window: int = 1,
) -> None:
    for chunk in chunks:
        chunk["neighboring_chunks"] = get_neighboring_chunks(
            matched_chunk=chunk,
            metadata=metadata,
            window=window,
        )

def score_without_reranker(query: str, chunk: dict, use_bm25: bool) -> float:
    bm25_component = 0.0
    if use_bm25:
        bm25_component = 0.30 * chunk["bm25_score_normalized"]

    return (
        0.60 * chunk["score_normalized"] +
        bm25_component +
        0.10 * chunk["metadata_boost_normalized"]
    )

def score_with_reranker(query: str, chunk: dict, use_bm25: bool) -> float:
    bm25_component = 0.0
    if use_bm25:
        bm25_component = 0.15 * chunk["bm25_score_normalized"]

    return (
        0.65 * chunk["rerank_score_normalized"] +
        0.15 * chunk["score_normalized"] +
        bm25_component +
        0.05 * chunk["metadata_boost_normalized"]
    )

def apply_reranker(query: str, chunks: list[dict], top_k: int) -> list[dict]:
    documents = [
        build_rerank_document(chunk, load_source_document(chunk))
        for chunk in chunks
    ]

    response = get_cohere_client().rerank(
        model=COHERE_RERANK_MODEL,
        query=query,
        documents=documents,
        top_n=min(top_k, len(documents)),
    )

    reranked = []
    for item in response.results:
        doc = chunks[item.index]
        doc["rerank_score"] = float(item.relevance_score)
        reranked.append(doc)

    return reranked

def search(
    query: str,
    top_k: int = 3,
    min_score: float | None = None,
    use_bm25: bool = True,
    use_reranker: bool = True,
    candidate_count: int | None = None,
) -> list[dict]:
    print(f"\nQuery: {query}\n")
    if candidate_count is None:
        candidate_count = max(DEFAULT_CANDIDATE_COUNT, top_k * DEFAULT_CANDIDATE_MULTIPLIER)
    candidate_count = max(candidate_count, top_k)

    chunks, metadata = find_faiss_candidates(query, candidate_count)
    if use_bm25:
        get_bm25_scores_for_candidates(query, chunks)

    for chunk in chunks:
        chunk["metadata_boost"] = metadata_boost(query, chunk)
    normalize_scores(chunks, "metadata_boost")

    if use_reranker:
        chunks = apply_reranker(query, chunks, top_k=candidate_count)
        normalize_scores(chunks, "rerank_score")
        for chunk in chunks:
            chunk["final_score"] = score_with_reranker(query, chunk, use_bm25)
    else:
        normalize_scores(chunks, "rerank_score")
        for chunk in chunks:
            chunk["final_score"] = score_without_reranker(query, chunk, use_bm25)

    if min_score is None:
        min_score = RERANK_MIN_SCORE if use_reranker else NO_RERANK_MIN_SCORE

    results = [
        chunk
        for chunk in chunks
        if chunk["final_score"] >= min_score
        and (
            not use_bm25
            or chunk["bm25_score_normalized"] >= BM25_NORMALIZED_MIN_SCORE
        )
        and (
            not use_reranker
            or chunk["rerank_score_normalized"] >= RERANK_NORMALIZED_MIN_SCORE
        )
    ]
    results.sort(key=lambda x: x["final_score"], reverse=True)
    results = dedupe_by_source(results)
    results.sort(key=lambda x: x["final_score"], reverse=True)
    results = results[:top_k]
    attach_neighboring_chunks(results, metadata)
    return results

def metadata_boost(query: str, chunk: dict) -> float:
    query_terms = set(query.lower().split())

    topic = chunk["topic"].lower()
    url = chunk["url"].lower()

    boost = 0.0

    if any(term in topic for term in query_terms):
        boost += 0.25

    if any(term in url for term in query_terms):
        boost += 0.25

    return boost

def load_answer_generator():
    try:
        from .AnswerGenerator import AnswerGenerator
    except ImportError:
        from AnswerGenerator import AnswerGenerator

    return AnswerGenerator

def read_prompt_template(prompt_file: str | None) -> str | None:
    if prompt_file is None:
        return None

    return Path(prompt_file).read_text(encoding="utf-8")

def print_search_results(results: list[dict]) -> None:
    print(f"Top {len(results)} results:\n")

    for index, result in enumerate(results, start=1):
        print(f"{index}. FAISS Score: {result['score']}")
        print(f"   FAISS Normalized: {result['score_normalized']}")
        print(f"   BM25 Score: {result['bm25_score']}")
        print(f"   BM25 Normalized: {result['bm25_score_normalized']}")
        print(f"   Rerank Score: {result['rerank_score']}")
        print(f"   Rerank Normalized: {result['rerank_score_normalized']}")
        print(f"   Metadata Boost: {result['metadata_boost']}")
        print(f"   Metadata Boost Normalized: {result['metadata_boost_normalized']}")
        print(f"   Final Score: {result['final_score']}")
        print(f"   Source: {result['source']}")
        print(f"   Document Directory: {result['document_dir']}")
        print(f"   Chunk ID: {result['chunk_id']}")
        print(f"   Topic: {result['topic']}")
        print(f"   URL: {result['url']}")
        print(f"   Text: {result['text']}")
        print()

def print_token_usage(usage, token_budget: int) -> None:
    input_tokens = usage.input_tokens or 0
    output_tokens = usage.output_tokens or 0
    cache_read_tokens = usage.cache_read_tokens or 0
    cache_write_tokens = usage.cache_write_tokens or 0
    total_tokens = input_tokens + output_tokens
    remaining_tokens = max(token_budget - total_tokens, 0)
    consumed_percentage = (total_tokens / token_budget * 100) if token_budget else 0.0

    print("\nToken Usage:\n")
    print(f"Input tokens: {input_tokens}")
    print(f"Output tokens: {output_tokens}")
    print(f"Total tokens: {total_tokens}")
    print(f"Cache read tokens: {cache_read_tokens}")
    print(f"Cache write tokens: {cache_write_tokens}")
    print(f"Token budget: {token_budget}")
    print(f"Budget consumed: {consumed_percentage:.2f}%")
    print(f"Budget remaining: {remaining_tokens}")

def generate_final_answer(args: argparse.Namespace, results: list[dict]) -> RAGResult:
    AnswerGenerator = load_answer_generator()
    prompt_template = read_prompt_template(args.answer_prompt_file)

    if prompt_template is None:
        generator = AnswerGenerator(
            model_name=args.answer_model,
            base_url=args.answer_base_url,
        )
    else:
        generator = AnswerGenerator(
            prompt_template=prompt_template,
            model_name=args.answer_model,
            base_url=args.answer_base_url,
        )

    return generator.generate_rag_result(
        query=args.query,
        search_results=results,
        max_context_results=args.answer_top_k,
        retries=args.answer_retries,
    )


def main() -> RAGResult:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--min-score", type=float, default=None)
    parser.add_argument(
        "--candidate-count",
        type=int,
        default=None,
        help="Number of FAISS candidates to fetch from each document category.",
    )
    parser.add_argument("--disable-bm25", action="store_true")
    parser.add_argument("--disable-reranker", action="store_true")
    parser.add_argument("--answer", action="store_true")
    parser.add_argument("--answer-top-k", type=int, default=3)
    parser.add_argument("--answer-retries", type=int, default=1)
    parser.add_argument("--answer-prompt-file", type=str, default=None)
    parser.add_argument("--answer-model", type=str, default="gemma3:12b")
    parser.add_argument("--answer-base-url", type=str, default="http://localhost:11434/v1")
    parser.add_argument(
        "--token-budget",
        type=int,
        default=8192,
        help="Maximum input-plus-output token budget used for monitoring.",
    )

    args = parser.parse_args()

    use_bm25 = not args.disable_bm25
    use_reranker = not args.disable_reranker

    print(f"BM25 enabled: {use_bm25}")
    print(f"Reranker enabled: {use_reranker}")
    query = args.query or query
    results = search(
        query,
        top_k=args.top_k,
        min_score=args.min_score,
        use_bm25=use_bm25,
        use_reranker=use_reranker,
        candidate_count=args.candidate_count,
    )
    #print_search_results(results)

    # if args.answer:
    #     generate_final_answer(args, results)
    generation_result = generate_final_answer(args, results)
    print("Final Answer:\n")
    print(generation_result.answer.model_dump_json(indent=2))
    print_token_usage(generation_result.usage, args.token_budget)
    return generation_result

if __name__ == "__main__":
    main()
