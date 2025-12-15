import plotly.express as px
import streamlit as st

from analytics import get_monthly_totals
from db import fetch_expenses
from ui.components import section_title


def render() -> None:
    st.title("Analysis")
    st.caption("Visualize where your money goes.")

    df = fetch_expenses()
    if df.empty:
        st.info("Add a few expenses first — charts will show up here.")
        return

    col1, col2 = st.columns([1, 1])

    with col1:
        section_title("Category distribution")
        by_category = (
            df.groupby("category", as_index=False)["amount"]
            .sum()
            .sort_values("amount", ascending=False)
        )
        fig_pie = px.pie(by_category, names="category", values="amount", hole=0.45)
        fig_pie.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig_pie, width="stretch")

    with col2:
        section_title("Monthly trend")
        monthly = get_monthly_totals(df)
        fig_line = px.line(monthly, x="month", y="total", markers=True)
        fig_line.update_layout(xaxis_title="Month", yaxis_title="Total")
        st.plotly_chart(fig_line, width="stretch")
