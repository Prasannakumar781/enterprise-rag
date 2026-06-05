from dotenv import load_dotenv
load_dotenv()

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI  # ✅ fixed: OpenAIEmbeddings from langchain_openai

# ✅ fixed: use same model as ingest.py and vector_store.py
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# ✅ fixed: use same collection_name as ingest.py and vector_store.py
db = Chroma(
    persist_directory="vectorstore",
    embedding_function=embeddings,
    collection_name="docs"
)

retriever = db.as_retriever(search_kwargs={"k": 3})

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

def ask(question: str):

    docs = retriever.invoke(question)  # ✅ already correct

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a helpful assistant. Use ONLY the context below.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [d.page_content for d in docs]
    }


if __name__ == "__main__":
    while True:
        q = input("\nAsk a question: ")
        if q.lower() in ["exit", "quit"]:
            break

        result = ask(q)

        print("\nAnswer:\n", result["answer"])