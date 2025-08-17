# db_connector.py — Simulated PostgreSQL data connector

from sqlalchemy import create_engine, text
import pandas as pd
import os

# Replace with real connection in production
MOCK_DATA_PATH = "data/diagnostics_sample.csv"

def connect_to_db():
    # In real app: use psycopg2 or SQLAlchemy w/ credentials
    # Example placeholder using CSV as mock data source
    if not os.path.exists(MOCK_DATA_PATH):
        raise FileNotFoundError("Mock diagnostic CSV not found in /data/")
    df = pd.read_csv(MOCK_DATA_PATH)
    return df

def run_query_simulated(question: str) -> pd.DataFrame:
    """
    Simulate query processing based on keyword match.
    Replace this with actual SQL logic later.
    """
    df = connect_to_db()

    # Dummy logic — filter dataframe based on question content
    if "model x" in question.lower():
        return df[df["model"] == "X"]
    elif "model y" in question.lower():
        return df[df["model"] == "Y"]
    elif "clutch" in question.lower():
        return df[df["issue"].str.contains("clutch", case=False)]
    else:
        return df.head(5)
