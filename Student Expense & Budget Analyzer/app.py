import streamlit as st

from db import init_db
from ui.navigation import sidebar_nav
from ui.styles import apply_styles
from views import add_expense, analysis, dashboard, insights, predictions


st.set_page_config(
	page_title="Student Expense & Budget Analyzer",
	page_icon="💸",
	layout="wide",
)

apply_styles()
init_db()


st.sidebar.title("Navigation")
items = {
	"Dashboard": ("home", "Dashboard"),
	"Add Expense": ("plus", "Add Expense"),
	"Analysis": ("pie", "Analysis"),
	"Predictions": ("trend", "Predictions"),
	"Insights": ("bulb", "Insights"),
}
page = sidebar_nav(items=items, default_label="Dashboard")
st.sidebar.markdown("---")
st.sidebar.caption("Data is stored locally in SQLite: expenses.db")


if page == "Dashboard":
	dashboard.render()
elif page == "Add Expense":
	add_expense.render()
elif page == "Analysis":
	analysis.render()
elif page == "Predictions":
	predictions.render()
elif page == "Insights":
	insights.render()
