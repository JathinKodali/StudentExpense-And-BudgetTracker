from __future__ import annotations

import sqlite3
from datetime import date as date_type
from pathlib import Path

import pandas as pd
import streamlit as st

DB_PATH = Path(__file__).with_name("expenses.db")


@st.cache_resource
def get_connection() -> sqlite3.Connection:
    # Streamlit reruns the script frequently; a cached connection keeps it fast.
    return sqlite3.connect(DB_PATH.as_posix(), check_same_thread=False)


def init_db() -> None:
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            description TEXT,
            amount REAL
        )
        """
    )
    conn.commit()


def insert_expense(expense_date: date_type, category: str, description: str, amount: float) -> None:
    conn = get_connection()
    conn.execute(
        "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
        (expense_date.isoformat(), category.strip(), description.strip(), float(amount)),
    )
    conn.commit()


def fetch_expenses() -> pd.DataFrame:
    conn = get_connection()
    df = pd.read_sql_query(
        "SELECT id, date, category, description, amount FROM expenses ORDER BY date ASC, id ASC",
        conn,
    )

    if df.empty:
        return df

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"]).copy()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0.0)
    df["category"] = df["category"].fillna("Uncategorized")
    df["description"] = df["description"].fillna("")
    df["month"] = df["date"].dt.to_period("M").astype(str)
    return df
