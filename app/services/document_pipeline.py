from app.services.parser import extract_text

from app.utils.chunking import chunk_text

from app.services.embeddings import (
    create_embeddings
)

from app.services.store_vectors import (
    store_embeddings
)

def process_document(pdf_path):

    print("Extracting text...")

    text = extract_text(pdf_path)

    print("Chunking text...")

    chunks = chunk_text(text)

    print(f"Total chunks: {len(chunks)}")

    print("Generating embeddings...")

    embeddings = create_embeddings(chunks)

    print("Storing vectors in FAISS...")

    store_embeddings(chunks, embeddings)

    return "Document Indexed Successfully"