import streamlit as st

from analytics import format_currency, get_monthly_totals
from db import fetch_expenses


def render() -> None:
    st.title("Insights")
    st.caption("Simple rules to help you optimize your budget.")

    df = fetch_expenses()
    if df.empty:
        st.info("Add expenses to receive personalized budget insights.")
        return

    total = float(df["amount"].sum())
    if total <= 0:
        st.info("Your total spending is 0. Add more data for insights.")
        return

    by_category = (
        df.groupby("category", as_index=False)["amount"]
        .sum()
        .sort_values("amount", ascending=False)
    )
    by_category["share"] = by_category["amount"] / total

    st.markdown("#### Category concentration")
    threshold = 0.35
    flagged = by_category.loc[by_category["share"] > threshold]

    if flagged.empty:
        st.success("Nice balance: no category exceeds 35% of your total spending.")
    else:
        st.warning("Some categories are taking a large share of your budget:")
        for _, row in flagged.iterrows():
            st.write(
                f"- **{row['category']}** is **{row['share']*100:.1f}%** "
                f"({format_currency(float(row['amount']))}) of your total spending."
            )
        st.info("Tip: try setting a category cap (e.g., weekly limit) and track it here.")

    st.markdown("#### Quick suggestions")
    top_category = by_category.iloc[0]["category"] if not by_category.empty else "-"
    st.write(f"- Your biggest spending category is **{top_category}**.")

    monthly = get_monthly_totals(df)
    if len(monthly) >= 2:
        prev_total = float(monthly.iloc[-2]["total"])
        curr_total = float(monthly.iloc[-1]["total"])
        if prev_total > 0 and curr_total > prev_total * 1.25:
            st.write(
                f"- Your spending increased by **{((curr_total/prev_total)-1)*100:.1f}%** "
                f"from {monthly.iloc[-2]['month']} to {monthly.iloc[-1]['month']}."
            )
            st.info("Tip: review recent categories and cut 1–2 non-essentials next month.")
        else:
            st.write("- Your month-to-month spending looks stable.")
