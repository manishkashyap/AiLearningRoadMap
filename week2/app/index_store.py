import json
from pathlib import Path

import numpy as np

from embedder import embed_texts


PROJECT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_DIR / "week2" / "data"


def build_index_for_chunk_dir(chunk_dir: Path) -> int:
    chunks_file = chunk_dir / "chunks.json"
    embeddings_file = chunk_dir / "embeddings.npy"
    metadata_file = chunk_dir / "metadata.json"

    chunks = json.loads(chunks_file.read_text(encoding="utf-8"))
    texts = [chunk["text"].strip(" \n") for chunk in chunks]

    if not texts:
        print(f"No chunks found in {chunks_file}.")
        return 0

    embeddings = embed_texts(texts)

    np.save(embeddings_file, embeddings)

    metadata = [
        {
            "chunk_id": chunk["chunk_id"],
            "source": chunk["source"],
            "document_dir": chunk.get("document_dir", chunk_dir.name),
            "topic": chunk["topic"],
            "url": chunk["url"],
            "text": chunk["text"],
        }
        for chunk in chunks
    ]

    metadata_file.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"Loaded {len(chunks)} chunks from {chunks_file}")
    print(f"Generated embeddings with shape: {embeddings.shape}")
    print(f"Saved embeddings to {embeddings_file}")
    print(f"Saved metadata to {metadata_file}")
    return len(chunks)


def build_index() -> None:
    chunk_dirs = sorted(
        path.parent
        for path in DATA_DIR.glob("*/chunks.json")
        if path.is_file()
    )

    if not chunk_dirs:
        print(f"No category chunk files found in {DATA_DIR}.")
        return

    total_chunks = 0
    for chunk_dir in chunk_dirs:
        print(f"\nProcessing {chunk_dir.name}")
        total_chunks += build_index_for_chunk_dir(chunk_dir)

    print(f"\nIndexed {total_chunks} chunks across {len(chunk_dirs)} document directories.")

if __name__ == "__main__":
    build_index()
