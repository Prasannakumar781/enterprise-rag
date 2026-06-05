from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
 
def get_vector_store():
    # ✅ already correct: uses text-embedding-3-small and collection_name="docs"
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
 
    db = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings,
        collection_name="docs"
    )
 
    return db.as_retriever(search_kwargs={"k": 3})