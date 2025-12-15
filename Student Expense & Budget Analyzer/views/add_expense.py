from datetime import date as date_type

import streamlit as st

from db import insert_expense
from ui.lottie import render_lottie, try_load_lottie


def render() -> None:
    st.title("Add Expense")
    st.caption("Log a new expense into your personal SQLite database.")

    categories = [
        "Food",
        "Transport",
        "Rent",
        "Books",
        "Entertainment",
        "Subscriptions",
        "Health",
        "Misc",
        "Other",
    ]

    with st.form("add-expense-form", clear_on_submit=True):
        col1, col2 = st.columns([1, 1])
        with col1:
            expense_date: date_type = st.date_input("Date", value=date_type.today())
            category = st.selectbox("Category", categories)
            custom_category = ""
            if category == "Other":
                custom_category = st.text_input("Custom category", placeholder="e.g., Coffee")

        with col2:
            description = st.text_input("Description", placeholder="e.g., Lunch at cafeteria")
            amount = st.number_input("Amount", min_value=0.01, step=10.0, format="%.2f")

        submitted = st.form_submit_button("Add expense")

    if not submitted:
        return

    final_category = (custom_category or category).strip() or "Uncategorized"
    if amount <= 0:
        st.error("Amount must be greater than 0.")
        return

    insert_expense(expense_date, final_category, description, float(amount))
    st.success("Saved! Expense added to your database.")
    render_lottie(
        try_load_lottie("https://assets10.lottiefiles.com/packages/lf20_jbrw3hcz.json"),
        height=180,
    )
