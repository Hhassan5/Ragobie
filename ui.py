import streamlit as st
from core.config import DEFAULT_MODELS, DEFAULT_EMBED_MODEL


def render_sidebar():
    with st.sidebar:
        st.subheader("Settings")
        model_name = st.selectbox("Groq Model", DEFAULT_MODELS)
        embed_model_name = st.text_input(
            "HuggingFace embedding model",
            value=DEFAULT_EMBED_MODEL,
            help="Any Sentence-Transformers model works; this one is light & fast.",
        )
        vectorstore_type = st.selectbox(
            "Vector Store Type",
            ["FAISS", "ChromaDB"],
            help="Choose which vector store backend to use."
        )
        chunk_size = st.slider("Chunk size", 300, 2000, 1000, 50)
        chunk_overlap = st.slider("Chunk overlap", 0, 400, 150, 10)
        k = st.slider("Top-k retrieved documents", 1, 10, 4, 1)
        show_sources = st.checkbox("Show retrieved chunks", value=True)

        st.markdown("---")
        st.subheader("Load PDFs")
        pdf_dir = st.text_input(
            "Optional: PDF directory path",
            value="",
            help="If provided, we'll load all PDFs in this folder.",
        )
        uploaded_files = st.file_uploader(
            "Or upload PDFs", type=["pdf"], accept_multiple_files=True
        )
        build_store = st.button("Build / Rebuild Vector Store")

    return {
        "model_name": model_name,
        "embed_model_name": embed_model_name,
        "vectorstore_type": vectorstore_type,
        "chunk_size": chunk_size,
        "chunk_overlap": chunk_overlap,
        "k": k,
        "show_sources": show_sources,
        "pdf_dir": pdf_dir,
        "uploaded_files": uploaded_files,
        "build_store": build_store,
    }


def render_chat_header():
    st.markdown("### Chat")
    user_q = st.text_input("Ask a question about your documents")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        ask_btn = st.button("Ask")
    with col2:
        clear_history = st.button("Clear Chat History")
    with col3:
        rebuild_chain = st.button("Rebuild Chain (use current store)")

    return user_q, ask_btn, clear_history, rebuild_chain


def render_answer_and_sources(result: dict, show_sources: bool):
    st.markdown("#### Answer")
    st.write(result.get("answer", ""))

    if show_sources:
        src_docs = result.get("source_documents", []) or []
        with st.expander("🔎 Retrieved Chunks (context)"):
            if not src_docs:
                st.write("No source documents returned.")
            else:
                for i, d in enumerate(src_docs, start=1):
                    meta = d.metadata or {}
                    st.markdown(
                        f"**Chunk {i}** • {meta.get('source','(unknown)')} • p.{meta.get('page', '?')}"
                    )
                    st.write(d.page_content)
                    st.markdown("---")
