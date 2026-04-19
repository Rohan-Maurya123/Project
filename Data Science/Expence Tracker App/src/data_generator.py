import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data(num_days=365):
    """
    Simulates realistic expense data with patterns.
    Seed is now random for each generation.
    """
    # Use system time for a truly random seed
    import time
    np.random.seed(int(time.time()))
    
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(num_days)]
    
    records = []
    
    categories = {
        "Food": (50, 200),
        "Travel": (500, 5000),
        "Rent": (15000, 20000),
        "Bills": (1000, 5000),
        "Shopping": (200, 3000),
        "Entertainment": (100, 1000),
        "Salary": (50000, 70000)
    }

    for date in dates:
        # 1. Monthly Rent & Bills (Fixed on 1st of each month)
        if date.day == 1:
            records.append({
                "Date": date,
                "Category": "Rent",
                "Amount": np.random.randint(*categories["Rent"]),
                "Type": "Expense",
                "Description": "Monthly House Rent"
            })
            records.append({
                "Date": date,
                "Category": "Bills",
                "Amount": np.random.randint(*categories["Bills"]),
                "Type": "Expense",
                "Description": "Electricity & Water"
            })
            # Monthly Salary
            records.append({
                "Date": date,
                "Category": "Salary",
                "Amount": np.random.randint(*categories["Salary"]),
                "Type": "Income",
                "Description": "Monthly Paycheck"
            })

        # 2. Daily Food (Higher on weekends)
        is_weekend = date.weekday() >= 5
        food_multiplier = 1.5 if is_weekend else 1.0
        records.append({
            "Date": date,
            "Category": "Food",
            "Amount": np.random.randint(*categories["Food"]) * food_multiplier,
            "Type": "Expense",
            "Description": "Daily Groceries/Dining"
        })

        # 3. Weekend Entertainment
        if is_weekend and np.random.random() > 0.4:
            records.append({
                "Date": date,
                "Category": "Entertainment",
                "Amount": np.random.randint(*categories["Entertainment"]),
                "Type": "Expense",
                "Description": "Movie/Outing"
            })

        # 4. Random Shopping (15% chance)
        if np.random.random() < 0.15:
            records.append({
                "Date": date,
                "Category": "Shopping",
                "Amount": np.random.randint(*categories["Shopping"]),
                "Type": "Expense",
                "Description": "Retail Therapy"
            })

        # 5. Occasional Travel (5% chance)
        if np.random.random() < 0.05:
            records.append({
                "Date": date,
                "Category": "Travel",
                "Amount": np.random.randint(*categories["Travel"]),
                "Type": "Expense",
                "Description": "Trip/Commute"
            })

    df = pd.DataFrame(records)
    # Shuffle the data
    df = df.sample(frac=1).reset_index(drop=True)
    
    import os
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/expenses.csv", index=False)
    print(f"Data Generated: {len(df)} records saved to data/expenses.csv")
    return df

if __name__ == "__main__":
    generate_data()