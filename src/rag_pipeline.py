# rag_pipeline.py — Handles RAG-based retrieval and generation

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter

import os

# Basic LLM and embedding models
llm = OpenAI(temperature=0.2)
embeddings = OpenAIEmbeddings()

# Utility to embed and store documents
def build_vector_index(docs):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)
    db = FAISS.from_documents(chunks, embeddings)
    return db

# Main function to query
def ask_insight(query, docs):
    vector_db = build_vector_index(docs)
    retriever = vector_db.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    response = qa_chain.run(query)
    return response
