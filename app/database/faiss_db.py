import faiss
import numpy as np

# Embedding dimension for all-MiniLM-L6-v2
dimension = 384

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Store document chunks
stored_chunks = []