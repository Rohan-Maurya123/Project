import pandas as pd

def get_response_counts(df):
    return df["Response"].value_counts()

def get_percentage(df):
    counts = get_response_counts(df)
    return (counts / len(df)) * 100

def region_analysis(df):
    return pd.crosstab(df["Region"], df["Response"])

def age_analysis(df):
    return pd.crosstab(df["Age_Group"], df["Response"])