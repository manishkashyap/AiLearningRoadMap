import torch
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentences = [
    "I want pricing details for WhatsApp campaigns.",
    "Please share commercial plans for messaging.",
    "My campaign is not sending emails.",
    "I want to schedule a product demo.",
    "The weather is nice today."
]

sentence_embedings = embedder.encode_document(sentences, convert_to_tensor=True)

for i, query in enumerate(sentences):
    query_embedding = embedder.encode_query(query, convert_to_tensor=True)
    for j in range(i+1, len(sentences)):
        query_embedding_2 = embedder.encode_query(sentences[j], convert_to_tensor=True)
        print(f"Query 1: {query}\n")
        print(f"Query 2: {sentences[j]}\n")
        similarity_scores = embedder.similarity(query_embedding, query_embedding_2)[0]
        print(f"{similarity_scores}\n")
