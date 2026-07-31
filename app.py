import streamlit as st
import tempfile

from app.services.document_pipeline import (
    process_document
)

from app.services.rag_pipeline import (
    generate_response
)

st.title("📄 AI Document Assistant")

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        tmp_file.write(
            uploaded_file.read()
        )

        pdf_path = tmp_file.name

    st.info("Processing document...")

    process_document(pdf_path)

    st.success(
        "Document indexed successfully!"
    )

# Ask Question
query = st.text_input(
    "Ask a question about the document"
)

if st.button("Generate Answer"):

    if query:

        result = generate_response(query)

        st.subheader("Answer")

        st.write(result["answer"])

        st.subheader("Similarity Score")

        st.write(
            result["similarity_score"]
        )