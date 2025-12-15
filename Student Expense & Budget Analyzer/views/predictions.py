import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression

from analytics import format_currency, get_monthly_totals
from db import fetch_expenses
from ui.components import Kpi, render_kpi_card


def render() -> None:
    st.title("Predictions")
    st.caption("A simple, explainable forecast based on your monthly history.")

    df = fetch_expenses()
    if df.empty:
        st.info("Add at least a few expenses to generate a prediction.")
        return

    monthly = get_monthly_totals(df)
    if len(monthly) < 2:
        st.warning("Need at least 2 months of data to train a Linear Regression model.")
        st.dataframe(monthly, width="stretch")
        return

    # Convert months to a sequential index (0, 1, 2, ...)
    X = np.arange(len(monthly)).reshape(-1, 1)
    y = monthly["total"].astype(float).values

    model = LinearRegression()
    model.fit(X, y)

    predicted_next_total = float(model.predict(np.array([[len(monthly)]]))[0])
    predicted_next_total = max(predicted_next_total, 0.0)

    last_month = monthly.iloc[-1]["month"]
    st.markdown("#### Next month prediction")
    render_kpi_card(
        Kpi(
            "Predicted Total Expense",
            format_currency(predicted_next_total),
            f"Trained on {len(monthly)} months (last: {last_month})",
        )
    )
