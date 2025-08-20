# 🚗 Generative AI Insight Assistant for Auto OEM Data

This project is inspired by real-world challenges at enterprise automotive clients (e.g., Tata Motors). It helps technical and non-technical stakeholders explore Aftermarket Reporting Metrics (ARM) — such as vehicle diagnostics, service tickets, and vendor feedback — using a conversational AI layer.

The assistant combines structured data (PostgreSQL) and unstructured insights (documents, feedback logs) using a **RAG (Retrieval-Augmented Generation)** pipeline.

---

## 💡 Key Features

- 🔍 **Natural language interface** to explore structured metrics & textual logs  
- ⚙️ **RAG pipeline** combining LangChain, FAISS, and OpenAI  
- 📊 **PostgreSQL integration** for structured metrics queries  
- 📄 **Doc loader support** (PDF, CSV, TXT) for internal reports  
- 🧪 **Streamlit UI** for quick deployment  

---

## 🛠 Tech Stack

- Python, Streamlit, LangChain, FAISS, OpenAI (GPT-4)
- PostgreSQL, SQLAlchemy
- Pandas, PyMuPDF (for PDF loading)

---

## 📂 Structure

├── src/
│ ├── main.py # Streamlit app entrypoint
│ ├── rag_pipeline.py # Core RAG logic
│ ├── db_connector.py # PostgreSQL connection + SQL queries
│ └── utils.py # File loaders, metadata utils
├── data/ # Placeholder for mock CSVs or SQLite dump
├── notebooks/ # EDA and prototyping notebooks
├── docs/ # Architecture diagrams
├── requirements.txt
└── README.md

🔗 [Link to Repo](https://github.com/Dhrvn/AutoGenAI-Insight) 

