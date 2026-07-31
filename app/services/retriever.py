import numpy as np

from sentence_transformers import SentenceTransformer

from app.database.faiss_db import (
    index,
    stored_chunks
)

# Load embedding model
model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def retrieve(query, top_k=5):

    # Convert query into embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(
        query_embedding,
        dtype=np.float32
    )

    # Search FAISS
    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(stored_chunks):

            results.append({
                "metadata": {
                    "text": stored_chunks[idx]
                }
            })

    return {
        "matches": results
    }