import pandas as pd

def clean_data(df):

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Make amount positive
    df["Amount"] = df["Amount"].abs()

    return df