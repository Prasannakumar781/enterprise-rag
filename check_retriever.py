from dotenv import load_dotenv
load_dotenv()

from app.retrievers.vector_store import get_vector_store

retriever = get_vector_store()
docs = retriever.invoke("What is the remote work policy?")

print(f"Found {len(docs)} docs")
for i, doc in enumerate(docs):
    print(f"\nDoc {i+1}:")
    print(doc.page_content)