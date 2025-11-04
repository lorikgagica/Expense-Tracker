# 💸 Expense Tracker CLI (Python)

A full-featured command-line tool for logging, analyzing, and visualizing your personal expenses. Enter expenses, see monthly summaries, get budget warnings, and export or analyze your finance data with ease!

---

## ✨ Features

- **Log expenses**: Date, category, amount, and custom description
- **View summary**: Group by category, see totals instantly
- **Pie chart**: Visualize where your money goes (by category)
- **Bar chart**: Monthly spending trends at a glance
- **Monthly budget alert**: Warns you if you exceed your planned spend for a month
- **Export**: Filter and export expenses by month/category
- **Top 3 categories**: Quick view and plot of the main areas you spend
- **Search by keyword**: Instantly find all matching entries by description
- **Daily average**: Calculate your daily spend for any month
- **Easy CLI menu**: All actions accessible from a simple numbered menu

---

## 🚀 How to Run

1. **Install Python 3** (if not already installed)
2. **Install required libraries:**
    ```
    pip install pandas matplotlib
    ```
3. **Save the code as `expense.py`**
4. **Run in terminal:**
    ```
    python expense.py
    ```

---

## 🧑‍💻 Usage

- Log new expenses by typing in the date, category, amount, and description
- View and plot summaries, budgets, top categories, and more from the menu
- Export any filtered subset (by month, by category, or both!) to CSV for backup or sharing

---

## 🗂️ How It Works

- **CSV for storage**: All expenses saved to `expenses.csv` (auto-created)
- **Pandas for analysis**, **matplotlib for graphs**
- **Menu options**:
    1. Log an Expense  
    2. View Expense Summary  
    3. Plot Expenses by Category  
    4. Plot Monthly Trends  
    5. Set/View Monthly Budget (with overspend warnings)
    6. Export Filtered Expenses  
    7. Show Top 3 Spending Categories  
    8. Search Expenses by Description  
    9. Daily Average Spend (by Month)  
    10. Exit

---

## 📄 License

MIT License — free for learning, teaching, and tinkering.

---

A beginner-friendly, practical Python project for managing your finances and learning data analysis!
