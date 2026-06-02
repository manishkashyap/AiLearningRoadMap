import json
from pathlib import Path
import numpy as np

from embedder import embed_texts


DATA_DIR = Path("/Users/manish/gitspace/AIRoadmap/week2/data")
CHUNKS_FILE = DATA_DIR / "chunks.json"
EMBEDDINGS_FILE = DATA_DIR / "embeddings.npy"
METADATA_FILE = DATA_DIR / "metadata.json"


def build_index() -> None:
    chunks = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))

    texts = [chunk["text"] for chunk in chunks]
    embeddings = embed_texts(texts)

    np.save(EMBEDDINGS_FILE, embeddings)

    metadata = [
        {
            "chunk_id": chunk["chunk_id"],
            "source": chunk["source"],
            "text": chunk["text"]
        }
        for chunk in chunks
    ]

    METADATA_FILE.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"Loaded {len(chunks)} chunks")
    print(f"Generated embeddings with shape: {embeddings.shape}")
    print(f"Saved embeddings to {EMBEDDINGS_FILE}")
    print(f"Saved metadata to {METADATA_FILE}")


if __name__ == "__main__":
    build_index()