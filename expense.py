import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import os

def log_expense(date, category, amount, description):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

def load_expenses():
    if not os.path.exists("expenses.csv"):
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    return pd.read_csv("expenses.csv", names=["Date", "Category", "Amount", "Description"])

def summarize_expenses(df):
    summary = df.groupby("Category")["Amount"].sum()
    print("\nExpense Summary by Category:\n", summary)

def plot_expenses_by_category(df):
    summary = df.groupby("Category")["Amount"].sum()
    summary.plot(kind="pie", autopct="%.1f%%", figsize=(8,8), title="Expenses by Category")
    plt.ylabel("")
    plt.show()

def plot_monthly_trends(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_summary = df.groupby("Month")["Amount"].sum()
    monthly_summary.plot(kind="bar", figsize=(10, 6), title="Monthly Expense Trends")
    plt.xlabel("Month")
    plt.ylabel("Total Expenses")
    plt.xticks(rotation=45)
    plt.show()

def set_monthly_budget(df):
    budget = float(input("Enter your monthly budget: "))
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_summary = df.groupby("Month")["Amount"].sum()
    print("\nMonthly Totals:")
    print(monthly_summary)
    # Budget warning
    for m, total in monthly_summary.items():
        if total > budget:
            print(f"⚠️  Warning: You exceeded the budget in {m} (Spent: {total}, Budget: {budget})")

def export_filtered(df):
    print("1. Filter by month\n2. Filter by category\n3. Both\n4. Cancel")
    fchoice = input("How do you want to filter and export? ")
    filtered = df.copy()
    if fchoice == "1" or fchoice == "3":
        month = input("Enter month (YYYY-MM): ")
        df["Date"] = pd.to_datetime(df["Date"])
        filtered = filtered[pd.to_datetime(filtered["Date"]).dt.to_period("M").astype(str) == month]
    if fchoice == "2" or fchoice == "3":
        category = input("Enter category: ")
        filtered = filtered[filtered["Category"] == category]
    if not filtered.empty:
        export_path = input("Enter filename for export (e.g., filtered_expenses.csv): ")
        filtered.to_csv(export_path, index=False)
        print(f"Exported {len(filtered)} expenses to {export_path}")
    else:
        print("No expenses matched the filter.")

def top_spending_categories(df):
    top_cats = df.groupby("Category")["Amount"].sum().nlargest(3)
    print("\nTop 3 Spending Categories:\n", top_cats)
    top_cats.plot(kind="bar", title="Top 3 Spending Categories")
    plt.xlabel("Category"), plt.ylabel("Amount")
    plt.show()

def search_expenses(df):
    keyword = input("Enter keyword to search in descriptions: ").lower()
    matches = df[df["Description"].str.lower().str.contains(keyword)]
    if not matches.empty:
        print("\nMatching Expenses:\n", matches)
    else:
        print("No matching expenses found.")

def daily_average(df):
    month = input("Enter month (YYYY-MM): ")
    df["Date"] = pd.to_datetime(df["Date"])
    filtered = df[df["Date"].dt.to_period("M").astype(str) == month]
    if filtered.empty:
        print("No data for that month.")
        return
    days = filtered["Date"].dt.day.nunique()
    avg = filtered["Amount"].sum() / days
    print(f"Daily average spend for {month}: {avg:.2f}")

def main():
    print("Welcome to the Expense Tracker!")
    while True:
        print("\n1. Log an Expense")
        print("2. View Expense Summary")
        print("3. Plot Expenses by Category")
        print("4. Plot Monthly Trends")
        print("5. Set/View Monthly Budget")
        print("6. Export Filtered Expenses")
        print("7. Show Top 3 Spending Categories")
        print("8. Search Expenses by Description")
        print("9. Daily Average Spend (by Month)")
        print("10. Exit")
        choice = input("Enter your choice: ")
        df = load_expenses()
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            log_expense(date, category, amount, description)
            print("Expense logged successfully!")
        elif choice == "2":
            summarize_expenses(df)
        elif choice == "3":
            plot_expenses_by_category(df)
        elif choice == "4":
            plot_monthly_trends(df)
        elif choice == "5":
            set_monthly_budget(df)
        elif choice == "6":
            export_filtered(df)
        elif choice == "7":
            top_spending_categories(df)
        elif choice == "8":
            search_expenses(df)
        elif choice == "9":
            daily_average(df)
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()