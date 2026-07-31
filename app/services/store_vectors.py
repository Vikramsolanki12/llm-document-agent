import numpy as np

from app.database.faiss_db import (
    index,
    stored_chunks
)

def store_embeddings(chunks, embeddings):

    # Convert embeddings to numpy float32
    embeddings_np = np.array(
        embeddings,
        dtype=np.float32
    )

    # Add vectors to FAISS
    index.add(embeddings_np)

    # Store corresponding chunks
    stored_chunks.extend(chunks)

    print(f"Stored {len(chunks)} chunks in FAISS")