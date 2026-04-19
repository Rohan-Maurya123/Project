import pandas as pd

def load_data(path="data/poll_data.csv"):
    return pd.read_csv(path)