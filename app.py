import streamlit as st
import pandas as pd
import os

DATA_FILE = "expenses.csv"

st.title("💰 Expense Tracker")

# Create CSV if not exists
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["date", "category", "amount", "description"])
    df.to_csv(DATA_FILE, index=False)

# Add Expense
st.header("Add New Expense")

date = st.date_input("Date")
category = st.selectbox(
    "Category",
    ["Food", "Travel", "Shopping", "Rent", "Entertainment", "Other"]
)
amount = st.number_input("Amount", min_value=0.0)
description = st.text_input("Description")

if st.button("Add Expense"):
    new_data = pd.DataFrame({
        "date": [date],
        "category": [category],
        "amount": [amount],
        "description": [description]
    })

    df = pd.read_csv(DATA_FILE)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

    st.success("Expense Added Successfully!")

# View Expenses
st.header("All Expenses")

df = pd.read_csv(DATA_FILE)

if not df.empty:
    st.dataframe(df)

    st.subheader("Category Wise Spending")
    cat = df.groupby("category")["amount"].sum()
    st.bar_chart(cat)

    st.subheader("Spending Distribution")
    st.pyplot(cat.plot.pie(autopct="%1.1f%%").figure)

else:
    st.info("No expenses added yet.")
