"""
Expense Tracker with Data Analysis
------------------------------------
A command-line expense tracker that stores expenses in a CSV file
and provides data analysis + visualizations using pandas and matplotlib.

Features:
- Add new expenses (date, category, amount, description)
- View all expenses
- Analyze spending by category, by month, and overall
- Generate charts (pie chart for categories, line chart for monthly trend)

Author: ChatGPT-style template, customize as needed.
"""

import csv
import os
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "expenses.csv"
FIELDNAMES = ["date", "category", "amount", "description"]


# ---------------------------------------------------------
# Data handling
# ---------------------------------------------------------
def init_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def add_expense(date, category, amount, description):
    """Append a new expense record to the CSV file."""
    with open(DATA_FILE, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        })
    print(f"Added expense: {date} | {category} | ${amount:.2f} | {description}")


def load_data():
    """Load expenses into a pandas DataFrame."""
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return pd.DataFrame(columns=FIELDNAMES)

    df = pd.read_csv(DATA_FILE)
    if df.empty:
        return df

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["date", "amount"])
    return df


# ---------------------------------------------------------
# Analysis
# ---------------------------------------------------------
def show_summary(df):
    """Print overall summary statistics."""
    if df.empty:
        print("No expense data available yet.")
        return

    total = df["amount"].sum()
    avg = df["amount"].mean()
    count = len(df)
    top_category = df.groupby("category")["amount"].sum().idxmax()

    print("\n--- Expense Summary ---")
    print(f"Total expenses recorded : {count}")
    print(f"Total amount spent      : ${total:,.2f}")
    print(f"Average expense amount  : ${avg:,.2f}")
    print(f"Top spending category   : {top_category}")
    print("------------------------\n")


def category_breakdown(df):
    """Return total spend per category, sorted descending."""
    if df.empty:
        return pd.Series(dtype=float)
    return df.groupby("category")["amount"].sum().sort_values(ascending=False)


def monthly_trend(df):
    """Return total spend per month."""
    if df.empty:
        return pd.Series(dtype=float)
    monthly = df.copy()
    monthly["month"] = monthly["date"].dt.to_period("M")
    return monthly.groupby("month")["amount"].sum().sort_index()


def plot_category_pie(df):
    """Pie chart of spending by category."""
    data = category_breakdown(df)
    if data.empty:
        print("No data to plot.")
        return

    plt.figure(figsize=(7, 7))
    plt.pie(data.values, labels=data.index, autopct="%1.1f%%", startangle=90)
    plt.title("Spending by Category")
    plt.tight_layout()
    plt.savefig("category_breakdown.png")
    print("Saved chart: category_breakdown.png")
    plt.close()


def plot_monthly_trend(df):
    """Line chart of monthly spending trend."""
    data = monthly_trend(df)
    if data.empty:
        print("No data to plot.")
        return

    plt.figure(figsize=(9, 5))
    data.index = data.index.astype(str)
    plt.plot(data.index, data.values, marker="o", linewidth=2)
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Spent ($)")
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("monthly_trend.png")
    print("Saved chart: monthly_trend.png")
    plt.close()


def plot_category_bar(df):
    """Bar chart comparing category totals."""
    data = category_breakdown(df)
    if data.empty:
        print("No data to plot.")
        return

    plt.figure(figsize=(9, 5))
    plt.bar(data.index, data.values, color="#4C72B0")
    plt.title("Total Spending per Category")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("category_bar.png")
    print("Saved chart: category_bar.png")
    plt.close()


# ---------------------------------------------------------
# CLI Menu
# ---------------------------------------------------------
def prompt_add_expense():
    print("\n-- Add New Expense --")
    date = input("Date (YYYY-MM-DD) [default: today]: ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    category = input("Category (e.g. Food, Rent, Travel): ").strip() or "Other"

    while True:
        amount_str = input("Amount: ").strip()
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Please enter a valid number.")

    description = input("Description: ").strip()
    add_expense(date, category, amount, description)


def main_menu():
    init_file()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Show summary")
        print("4. Category breakdown (table)")
        print("5. Monthly trend (table)")
        print("6. Generate charts (pie, bar, trend)")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            prompt_add_expense()

        elif choice == "2":
            df = load_data()
            if df.empty:
                print("No expenses recorded yet.")
            else:
                print(df.sort_values("date").to_string(index=False))

        elif choice == "3":
            df = load_data()
            show_summary(df)

        elif choice == "4":
            df = load_data()
            data = category_breakdown(df)
            print("\n--- Category Breakdown ---")
            print(data.to_string() if not data.empty else "No data available.")

        elif choice == "5":
            df = load_data()
            data = monthly_trend(df)
            print("\n--- Monthly Trend ---")
            print(data.to_string() if not data.empty else "No data available.")

        elif choice == "6":
            df = load_data()
            plot_category_pie(df)
            plot_category_bar(df)
            plot_monthly_trend(df)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main_menu()
