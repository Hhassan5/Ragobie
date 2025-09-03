# rag_app/config.py
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Defaults used in the sidebar
DEFAULT_MODELS = ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "llama3-70b-8192"]
DEFAULT_EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Local temp folder for uploads
TMP_UPLOAD_DIR = ".tmp_uploads"


def set_page():
    """Minimal Streamlit page configuration and title."""
    st.set_page_config(page_title="RAG FIASS Chatbot", page_icon="🤖", layout="wide")
    st.title("RAG Chatbot Groq + HuggingFace + FAISS")
