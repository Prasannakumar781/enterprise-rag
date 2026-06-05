import logging
from langchain_openai import ChatOpenAI
from app.retrievers.vector_store import get_vector_store

logger = logging.getLogger("rag-system")

# ✅ lazy init to avoid crash if vectorstore is missing at startup
_retriever = None
_llm = None

def _get_retriever():
    global _retriever
    if _retriever is None:
        _retriever = get_vector_store()
    return _retriever

def _get_llm():
    global _llm
    if _llm is None:
        _llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    return _llm

def ask_question(question: str):

    try:
        retriever = _get_retriever()
        llm = _get_llm()

        # ✅ fixed: replaced deprecated get_relevant_documents() with invoke()
        docs = retriever.invoke(question)

        if not docs:
            return {
                "answer": "No relevant documents found.",
                "sources": []
            }

        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
You are a strict RAG assistant.

Rules:
- Answer ONLY using the context below.
- If not found in context, say you don't know.

Context:
{context}

Question:
{question}

Answer:
"""

        response = llm.invoke(prompt)

        return {
            "answer": response.content,
            "sources": [d.page_content for d in docs]
        }

    except Exception as e:
        logger.error(f"Error in RAG pipeline: {str(e)}")       
        return {
            "answer": "Sorry, I couldn't process your request.",
            "sources": []
        }