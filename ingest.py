from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma  # ✅ fixed: use langchain_chroma, not langchain_community

print("Loading document...")

loader = TextLoader("data/company_handbook.txt")
documents = loader.load()

print(f"Loaded {len(documents)} document(s)")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# ✅ fixed: use same model as vector_store.py
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# ✅ fixed: use same collection_name as vector_store.py
db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="vectorstore",
    collection_name="docs"
)

print("Vector database created successfully!")