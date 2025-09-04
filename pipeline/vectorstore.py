from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS, Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def build_vectorstore(docs, embed_model_name: str, vectorstore_type: str, chunk_size: int, chunk_overlap: int):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    splits = text_splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings(model_name=embed_model_name)
    if vectorstore_type == "ChromaDB":
        return Chroma.from_documents(splits, embeddings)
    elif vectorstore_type == "FAISS":
        return FAISS.from_documents(splits, embeddings)
    else:
        raise ValueError(f"Unsupported vectorstore type: {vectorstore_type}")
