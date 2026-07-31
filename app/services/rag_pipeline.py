import os

from groq import Groq

from dotenv import load_dotenv

from app.services.retriever import retrieve

from app.services.similarity import (
    calculate_similarity
)

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_response(query):

    # Retrieve relevant chunks
    results = retrieve(query)

    context = ""

    for match in results["matches"]:

        context += (
            match["metadata"]["text"]
            + "\n"
        )

    if context.strip() == "":

        return {
            "answer": "No relevant information found.",
            "similarity_score": 0
        }

    prompt = f"""
    You are a helpful AI assistant.

    Use ONLY the provided context.

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=1000
    )

    answer = response.choices[0].message.content

    similarity_score = calculate_similarity(
        query,
        answer
    )

    return {
        "answer": answer,
        "similarity_score": float(similarity_score)
    }