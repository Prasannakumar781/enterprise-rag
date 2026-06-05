from fastapi import FastAPI
from app.schemas.request import QueryRequest
from app.services.rag_service import ask_question

app = FastAPI(
    title="Enterprise RAG System",
    description="RAG-powered Q&A over company documents",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/ask")
def ask(request: QueryRequest):
    return ask_question(request.question)