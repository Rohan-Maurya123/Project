import pandas as pd
import random
from datetime import datetime, timedelta

categories = [
    "Food", "Transport", "Shopping",
    "Entertainment", "Bills", "Healthcare"
]

payment_methods = [
    "Cash", "UPI", "Credit Card", "Debit Card"
]

def generate_expense_data():

    data = []

    start_date = datetime(2025, 5, 5)

    for i in range(300):

        date = start_date + timedelta(days=random.randint(0, 365))

        record = {
            "Date": date.strftime("%Y-%m-%d"),
            "Category": random.choice(categories),
            "Amount": round(random.uniform(100, 5000), 2),
            "Payment_Method": random.choice(payment_methods),
            "Description": f"Expense {i}"
        }

        data.append(record)

    df = pd.DataFrame(data)

    df.to_csv("data/expenses.csv", index=False)

    print("Expense Dataset Generated")