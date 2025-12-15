import pandas as pd
import streamlit as st

from analytics import format_currency, get_current_month_key
from db import fetch_expenses
from ui.components import Kpi, render_kpi_card
from ui.lottie import render_lottie, try_load_lottie


def render() -> None:
    st.title("Dashboard")
    st.caption("A quick snapshot of your spending.")

    left, right = st.columns([2, 1])
    with right:
        render_lottie(
            try_load_lottie("https://assets1.lottiefiles.com/packages/lf20_myejiggj.json"),
            height=220,
        )

    df = fetch_expenses()
    if df.empty:
        with left:
            st.info("No expenses yet. Go to **Add Expense** to start tracking!")
        return

    total_expenses = float(df["amount"].sum())

    current_month = get_current_month_key()
    monthly_expenses = float(df.loc[df["month"] == current_month, "amount"].sum())

    by_category = (
        df.groupby("category", as_index=False)["amount"]
        .sum()
        .sort_values("amount", ascending=False)
    )
    top_category = by_category.iloc[0]["category"] if not by_category.empty else "-"
    top_category_amount = float(by_category.iloc[0]["amount"]) if not by_category.empty else 0.0

    with left:
        k1, k2, k3 = st.columns(3)
        with k1:
            render_kpi_card(Kpi("Total Expenses", format_currency(total_expenses), "All time"))
        with k2:
            render_kpi_card(Kpi("Monthly Expenses", format_currency(monthly_expenses), f"This month ({current_month})"))
        with k3:
            render_kpi_card(Kpi("Top Category", str(top_category), format_currency(top_category_amount)))

        st.divider()
        st.markdown("#### Recent entries")
        preview = df.sort_values(["date", "id"], ascending=[False, False]).head(10).copy()
        preview["date"] = pd.to_datetime(preview["date"]).dt.date
        st.dataframe(preview[["date", "category", "description", "amount"]], width="stretch")
