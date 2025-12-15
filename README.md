🎓 Student Expense & Budget Analyzer

A modern, data-driven web application that helps students track expenses, analyze spending patterns, predict future expenses, and optimize budgets using interactive dashboards and machine learning.

🚀 Features

📥 Expense Tracking
Add daily expenses with category, description, and amount.

🗂️ Persistent Storage
Stores all expense data securely using SQLite.

📊 Spending Analysis
Visualize category-wise and monthly expense trends with interactive charts.

🔮 Expense Prediction
Forecast next month’s expenses using a machine learning model (Linear Regression).

💡 Budget Optimization Insights
Get data-driven recommendations when spending exceeds healthy limits.

🎨 Modern UI & Animations
Clean Streamlit interface with custom CSS, Plotly charts, and optional Lottie animations.

🛠️ Tech Stack

Language: Python

Frontend: Streamlit

Database: SQLite

Data Analysis: Pandas, NumPy

Machine Learning: Scikit-learn

Visualization: Plotly

UI Enhancements: Custom CSS, Lottie Animations

📂 Project Structure
student-expense-analyzer/
│
├── app.py
├── database/
│   └── expense_db.py
├── data/
│   └── expenses.db
├── animations/
│   └── money.json
├── utils/
│   ├── analysis.py
│   ├── forecasting.py
│   └── recommendations.py
├── requirements.txt
└── README.md

▶️ How to Run Locally
git clone https://github.com/your-username/student-expense-analyzer.git
cd student-expense-analyzer
pip install -r requirements.txt
streamlit run app.py

📈 Use Case

This project demonstrates how data analytics and machine learning can be applied to solve real-world budgeting problems faced by students. It is designed to be simple, explainable, and scalable, making it suitable for academic projects, internships, and entry-level data roles.

🧠 Future Enhancements

User authentication (multi-user support)

Advanced time-series forecasting

Expense category auto-classification using NLP

Cloud deployment with persistent storage

Export insights as PDF/CSV reports
