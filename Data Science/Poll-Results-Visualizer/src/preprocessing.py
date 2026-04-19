def clean_data(df):
    df = df.copy()
    df.dropna(inplace=True)
    return df