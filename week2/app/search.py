import json
from pathlib import Path
import argparse

import faiss
import numpy

from embedder import embed_texts

DATA_DIR = Path("/Users/manish/gitspace/AIRoadmap/week2/data")
CHUNKS_FILE = DATA_DIR / "chunks.json"
EMBEDDINGS_FILE = DATA_DIR / "embeddings.npy"
METADATA_FILE = DATA_DIR / "metadata.json"

def search(query: str, top_k: int = 3, min_score: float = 0.25) -> list[dict]:
    embeddings = numpy.load(EMBEDDINGS_FILE).astype("float32")
    metadata = json.loads(METADATA_FILE.read_text(encoding="utf-8"))

    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    print(f"\nQuery: {query}\n")
    query_embedding = embed_texts([query]).astype("float32")
    scores, ranked_indices = index.search(query_embedding, k=top_k)

    chunks = []
    seen_sources = set()

    for score, idx in zip(scores[0], ranked_indices[0]):
        score = float(score)

        if score < min_score:
            continue

        item = metadata[idx]

        # optional source-level dedupe
        dedupe_key = item["chunk_id"]
        if dedupe_key in seen_sources:
            continue

        seen_sources.add(dedupe_key)

        chunks.append({
            "score": round(score, 4),
            "chunk_id": item["chunk_id"],
            "source": item["source"],
            "text": item["text"]
        })

        if len(chunks) >= top_k:
            break
    return chunks

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--min-score", type=float, default=0.25)

    args = parser.parse_args()

    results = search(args.query, args.top_k, args.min_score)
    print(f"Top {len(results)} results:\n")

    for index, result in enumerate(results, start=1):
        print(f"{index}. Score: {result['score']}")
        print(f"   Source: {result['source']}")
        print(f"   Chunk ID: {result['chunk_id']}")
        print(f"   Text: {result['text']}")
        print()


if __name__ == "__main__":
    main()
