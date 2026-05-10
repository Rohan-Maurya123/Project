# src/data_loader.py

import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, start, end):
    """
    Download stock data from Yahoo Finance
    """

    df = yf.download(ticker, start=start, end=end)

    df.reset_index(inplace=True)

    return df


def load_csv_data(path):
    """
    Load stock data from CSV
    """

    df = pd.read_csv(path)

    return df