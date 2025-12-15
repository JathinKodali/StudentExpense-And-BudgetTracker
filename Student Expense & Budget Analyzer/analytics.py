from __future__ import annotations

import pandas as pd


def format_currency(amount: float) -> str:
    # Keep formatting simple and student-friendly.
    return f"₹{amount:,.2f}"


def get_current_month_key() -> str:
    return pd.Timestamp.today().to_period("M").strftime("%Y-%m")


def get_monthly_totals(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=["month", "total"])

    monthly = (
        df.groupby("month", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total"})
        .sort_values("month")
    )
    return monthly
