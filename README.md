# Enterprise RAG System 🤖📚

This is a Retrieval-Augmented Generation (RAG) system built using LangChain, OpenAI, and ChromaDB.

---

## 🚀 Features

- Document-based question answering
- Vector database using ChromaDB
- OpenAI embeddings for semantic search
- GPT-4o-mini for response generation
- Simple CLI chatbot interface

---

## 🧠 How it works

1. Documents are split into chunks
2. Each chunk is converted into embeddings
3. Stored in Chroma vector database
4. User question is embedded
5. Similar chunks are retrieved
6. GPT generates answer using retrieved context

---

## 📁 Project Structure
app/
retrievers/
services/
vectorstore/
rag.py
.env


---

## ⚙️ Setup Instructions

### 1. Clone repo

git clone https://github.com/your-username/enterprise-rag.git


### 2. Install dependencies

pip install -r requirements.txt


### 3. Add environment variables
Create `.env` file:

OPENAI_API_KEY=your_api_key_here


### 4. Run the app

python rag.py


---

## 🔐 Security Note

- Never upload `.env` file
- API keys must remain private

---

## 🛠 Tech Stack

- Python
- LangChain
- OpenAI GPT-4o-mini
- ChromaDB

---

## 📌 Future Improvements

- Web UI (Streamlit / FastAPI)
- Reranking for better accuracy
- Multi-document support
- PDF upload feature

---

## 👨‍💻 Author

Built by Arditi
💾 Save file
Click File → Save
Close Notepad
🚀 OPTION 2: Push README to GitHub

Now run:

git add README.md
git commit -m "add README"
git push
