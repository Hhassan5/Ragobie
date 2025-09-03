import streamlit as st
from langchain.memory import ConversationBufferMemory

def create_memory():
    return ConversationBufferMemory(
    memory_key="chat_history",
    input_key="question",
    output_key="answer",
    return_messages=True,
    )

def init_session_state():
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None
    if "memory" not in st.session_state:
        st.session_state.memory = create_memory()
    if "retriever" not in st.session_state:
        st.session_state.retriever = None
    if "chain" not in st.session_state:
        st.session_state.chain = None


def reset_memory():
    st.session_state.memory = create_memory()
