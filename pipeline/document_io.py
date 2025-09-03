import os
from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader


def load_pdfs_from_directory(pdf_dir_path: str):
    docs = []
    if pdf_dir_path and os.path.isdir(pdf_dir_path):
        dir_loader = PyPDFDirectoryLoader(pdf_dir_path)
        docs.extend(dir_loader.load())
    return docs


def load_pdfs_from_uploads(uploaded_files, tmp_dir: str):
    docs = []
    if uploaded_files:
        os.makedirs(tmp_dir, exist_ok=True)
        for up in uploaded_files:
            tmp_path = os.path.join(tmp_dir, up.name)
            with open(tmp_path, "wb") as f:
                f.write(up.getbuffer())
            docs.extend(PyPDFLoader(tmp_path).load())
    return docs


def load_pdfs_from_inputs(pdf_dir_path: str, uploaded_files, tmp_dir: str):
    docs = []
    docs.extend(load_pdfs_from_directory(pdf_dir_path))
    docs.extend(load_pdfs_from_uploads(uploaded_files, tmp_dir))
    return docs
