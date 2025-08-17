# utils.py — Document loader for PDFs, CSVs, and text files

# utils.py — Document loader for PDFs, CSVs, and text files

from langchain_community.document_loaders import PyMuPDFLoader, TextLoader, CSVLoader
from langchain.docstore.document import Document
import tempfile
import os


def load_file(uploaded_file):
    # Save uploaded file to a temp location
    suffix = "." + uploaded_file.name.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    # Determine file type
    if uploaded_file.name.endswith(".pdf"):
        loader = PyMuPDFLoader(tmp_path)
    elif uploaded_file.name.endswith(".csv"):
        loader = CSVLoader(file_path=tmp_path)
    elif uploaded_file.name.endswith(".txt"):
        loader = TextLoader(file_path=tmp_path)
    else:
        raise ValueError("Unsupported file format")

    docs = loader.load()

    # Optional: clean up temp file
    os.remove(tmp_path)

    return docs
