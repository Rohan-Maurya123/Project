import pandas as pd

def clean_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.dropna()
    df = df.sort_values('Date')
    return df