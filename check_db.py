from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = Chroma(persist_directory="vectorstore", embedding_function=embeddings, collection_name="docs")
results = db.get()

print(f"Total chunks: {len(results['documents'])}")
print()
for i, doc in enumerate(results['documents']):
    print(f"Chunk {i+1}:")
    print(doc[:300])
    print("---")