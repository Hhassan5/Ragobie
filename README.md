# 🤖 RAG Chatbot (Groq + HuggingFace + FAISS/Chroma)

A **Retrieval-Augmented Generation (RAG) chatbot** built with [LangChain](https://www.langchain.com/), [Groq LLM API](https://groq.com/), [HuggingFace embeddings](https://huggingface.co/sentence-transformers), and vector databases (**FAISS** or **ChromaDB**).  
The chatbot lets you upload PDFs, build a vector store, and query your documents interactively.

---

## ✨ Features
- ⚡ Fast LLM inference via **Groq API**
- 📑 Upload **single or multiple PDFs** or load from a directory
- 🧩 Choice of vector store: **FAISS** or **ChromaDB**
- 🔎 Configurable chunk size, overlap, and top-k retrieval
- 💬 Conversational memory (LangChain buffer memory)
- 📖 Option to display retrieved chunks for transparency

---

## 📸 Demo

### UI in action
<img width="1919" height="921" alt="Screenshot 2025-09-03 195446" src="https://github.com/user-attachments/assets/14da754e-a0e6-4b51-ab76-db124fe1d5d7" />

### Example PDF Answering
<img width="538" height="559" alt="Screenshot 2025-09-03 195719" src="https://github.com/user-attachments/assets/17adca8b-252b-40a7-ab07-f2e3a247fa7f" />

---

## 🛠️ Installation

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/your-username/ragobie.git
cd ragobie
python -m venv .venv
source .venv/bin/activate   # (Linux/Mac)
.venv\Scripts\activate      # (Windows)
pip install -r requirements.txt
