import pandas as pd
import numpy as np

def clean_data(file_path="data/expenses.csv"):
    """
    Cleans the raw data and performs feature engineering.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

    # 1. Basic Cleaning
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['Date', 'Amount', 'Category'], inplace=True)

    # 2. Type Conversion
    df['Date'] = pd.to_datetime(df['Date'])
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df.dropna(subset=['Amount'], inplace=True) # Remove rows with non-numeric amounts

    # 3. Standardization
    df['Category'] = df['Category'].str.strip().str.title()
    df['Type'] = df['Type'].str.strip().str.title()
    df['Description'] = df['Description'].str.strip()

    # 4. Feature Engineering
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month_name()
    df['Month_Num'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['Weekday'] = df['Date'].dt.day_name()
    df['Is_Weekend'] = df['Date'].dt.weekday >= 5
    df['Year_Month'] = df['Date'].dt.to_period('M').astype(str)

    # Sort by date
    df.sort_values(by='Date', inplace=True)

    # Save cleaned data
    import os
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/cleaned_expenses.csv", index=False)
    print(f"Data Cleaned: {len(df)} records saved to data/cleaned_expenses.csv")
    return df

if __name__ == "__main__":
    clean_data()