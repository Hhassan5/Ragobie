import time
import streamlit as st

from core.config import set_page, GROQ_API_KEY, TMP_UPLOAD_DIR
from core.state import init_session_state, reset_memory
from pipeline.document_io import load_pdfs_from_inputs
from pipeline.vectorstore import build_vectorstore
from pipeline.chain import make_chain
import ui


def main():
    # Page + initial state
    set_page()
    init_session_state()

    # Sidebar controls and actions
    sidebar = ui.render_sidebar()
    st.session_state["show_sources"] = sidebar["show_sources"]

    # Build/Rebuild vector store
    if sidebar["build_store"]:
        with st.spinner("Loading PDFs and building vector store..."):
            docs = load_pdfs_from_inputs(
                sidebar["pdf_dir"], sidebar["uploaded_files"], TMP_UPLOAD_DIR
            )
            if not docs:
                st.error("No PDFs found (directory or uploads). Please add some.")
            else:
                st.session_state.vectorstore = build_vectorstore(
                    docs=docs,
                    embed_model_name=sidebar["embed_model_name"],
                    vectorstore_type=sidebar["vectorstore_type"],
                    chunk_size=sidebar["chunk_size"],
                    chunk_overlap=sidebar["chunk_overlap"],
                )
                st.session_state.chain, st.session_state.retriever = make_chain(
                    vectorstore=st.session_state.vectorstore,
                    model_name=sidebar["model_name"],
                    k=sidebar["k"],
                    memory=st.session_state.memory,
                    api_key=GROQ_API_KEY,
                )
                st.success(f"{sidebar['vectorstore_type']} Vector store ready ✅ | {len(docs)} chunks loaded.")

    # Chat controls
    user_q, ask_btn, clear_history, rebuild_chain = ui.render_chat_header()

    if clear_history:
        reset_memory()
        if st.session_state.vectorstore:
            st.session_state.chain, st.session_state.retriever = make_chain(
                vectorstore=st.session_state.vectorstore,
                model_name=sidebar["model_name"],
                k=sidebar["k"],
                memory=st.session_state.memory,
                api_key=GROQ_API_KEY,
            )
        st.info("Chat history cleared.")

    if rebuild_chain and st.session_state.vectorstore:
        st.session_state.chain, st.session_state.retriever = make_chain(
            vectorstore=st.session_state.vectorstore,
            model_name=sidebar["model_name"],
            k=sidebar["k"],
            memory=st.session_state.memory,
            api_key=GROQ_API_KEY,
        )
        st.success("Chain rebuilt.")

    if ask_btn:
        if not st.session_state.chain:
            st.warning("Please build the vector store first (sidebar).")
        elif not user_q.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Retrieving + generating..."):
                t0 = time.perf_counter()
                result = st.session_state.chain.invoke({"question": user_q})
                dt = time.perf_counter() - t0

            st.markdown(f"**Response time:** {dt:.2f}s")
            ui.render_answer_and_sources(result, sidebar["show_sources"])


if __name__ == "__main__":
    main()
