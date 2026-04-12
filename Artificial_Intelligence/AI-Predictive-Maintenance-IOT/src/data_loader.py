import pandas as pd

def load_data():
 
    columns = ['unit', 'cycle'] + \
              [f'op_setting_{i}' for i in range(1, 4)] + \
              [f'sensor_{i}' for i in range(1, 22)]

    # Load NASA dataset
    df = pd.read_csv("data/train_FD001.txt", sep=" ", header=None)

    df = df.dropna(axis=1)

    df.columns = columns

    print("Data Loaded Successfully")
    return df