# main.py — Streamlit UI for Generative Insight Assistant
# main.py — Streamlit UI for Generative Insight Assistant

import os, sys
from pathlib import Path

# Ensure project root is on sys.path so "src.*" imports work on Streamlit Cloud
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from src.rag_pipeline import ask_insight
    from src.utils import load_file
except ModuleNotFoundError:
    # Fallback if working dir is project root
    from rag_pipeline import ask_insight
    from utils import load_file

import streamlit as st

st.set_page_config(page_title="AutoGenAI Insight Assistant", layout="wide")

st.title("🚗 AutoGenAI — Conversational OEM Insight Assistant")
st.markdown("Ask me questions about service logs, diagnostics, and ARM data. I’ll combine structured + unstructured sources.")

# File uploader for unstructured docs
uploaded_files = st.file_uploader("Upload internal documents (PDF, CSV, TXT)", accept_multiple_files=True)

if uploaded_files:
    docs = []
    for file in uploaded_files:
        st.info(f"Processing {file.name}")
        loaded = load_file(file)
        docs.extend(loaded)

    st.success(f"Loaded {len(docs)} document chunks into memory.")

    # Ask a question
    user_q = st.text_input("🔍 Ask a question", placeholder="e.g. What were the top complaints about Model Y brakes?")
    if user_q:
        with st.spinner("Generating insight..."):
            response = ask_insight(user_q, docs)
            st.markdown("### 🧠 Insight")
            st.write(response)
