# src/data_cleaning.py

import pandas as pd


def clean_data(df):
    """
    Clean stock dataframe
    """

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Forward fill missing values
    df = df.ffill()

    # Backward fill remaining missing values
    df = df.bfill()

    # Reset index
    df.reset_index(drop=True, inplace=True)

    return df