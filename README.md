# 📚 RAG Chatbot (Groq + HuggingFace + FAISS)

A **Retrieval-Augmented Generation (RAG) chatbot** built with [LangChain](https://www.langchain.com/), [Groq LLM API](https://groq.com/), [HuggingFace embeddings](https://huggingface.co/sentence-transformers), and [FAISS](https://github.com/facebookresearch/faiss).  
The chatbot lets you upload PDFs, build a local vector store, and query your documents interactively.

---

## ✨ Features
- ⚡ Fast LLM inference using **Groq API**  
- 🔎 Document search powered by **FAISS**  
- 📑 Supports **PDF uploads & directories**  
- 🧩 Configurable chunk size, overlap, and top-k retrieval  
- 💬 Conversational memory using LangChain  
- 📖 Displays retrieved document chunks for transparency  

---

## 📸 Demo

### UI in action
![App Screenshot](./assets/Screenshot_2025-09-03_195446.png)

### Example PDF Answering
![PDF QA Screenshot](./assets/Screenshot_2025-09-03_195719.png)

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
