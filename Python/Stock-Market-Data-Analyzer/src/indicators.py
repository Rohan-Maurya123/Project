# src/indicators.py

import numpy as np


def calculate_daily_returns(df):

    df["Daily_Return"] = df["Close"].pct_change()

    return df


def moving_averages(df, short_window=20, long_window=50):

    df["MA_Short"] = df["Close"].rolling(window=short_window).mean()

    df["MA_Long"] = df["Close"].rolling(window=long_window).mean()

    return df


def calculate_volatility(df):

    volatility = df["Daily_Return"].std() * np.sqrt(252)

    return volatility


def highest_lowest_price(df):

    highest = df["High"].max()

    lowest = df["Low"].min()

    return highest, lowest