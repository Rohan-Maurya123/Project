import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # Fix TotalCharges issue
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    df.dropna(inplace=True)

    # Convert target
    df["Churn"] = df["Churn"].map({"Yes":1, "No":0})

    return df


def encode_data(df):
    df = pd.get_dummies(df, drop_first=True)
    return df