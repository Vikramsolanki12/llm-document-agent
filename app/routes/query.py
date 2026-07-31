from fastapi import APIRouter
from pydantic import BaseModel

from app.services.rag_pipeline import generate_response

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/query")

def query_docs(request: QueryRequest):

    answer = generate_response(request.query)

    return {
        "query": request.query,
        "answer": answer
    }