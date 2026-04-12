import pandas as pd
import numpy as np


def load_and_clean(path):
    df = pd.read_csv(path)

    df.replace('?', np.nan, inplace=True)

    cols = [
        'Global_active_power',
        'Global_reactive_power',
        'Voltage',
        'Global_intensity',
        'Sub_metering_1',
        'Sub_metering_2',
        'Sub_metering_3'
    ]

    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna()

    # datetime
    df['Datetime'] = pd.to_datetime(
        df['Date'] + ' ' + df['Time'],
        errors='coerce',
        dayfirst=True
    )

    df = df.dropna(subset=['Datetime'])
    df = df.sort_values('Datetime')

    # features
    df['hour'] = df['Datetime'].dt.hour
    df['day'] = df['Datetime'].dt.day
    df['month'] = df['Datetime'].dt.month
    df['weekday'] = df['Datetime'].dt.weekday

    # lag features (safe version)
    df['lag1'] = df['Global_active_power'].shift(1)
    df['lag2'] = df['Global_active_power'].shift(2)
    df['rolling_mean'] = df['Global_active_power'].rolling(5).mean()

    df = df.dropna()

    return df


def get_features(df):
    X = df[['hour', 'day', 'month', 'weekday', 'lag1', 'lag2', 'rolling_mean']]
    y = df['Global_active_power']
    return X, y



def time_split(X, y, ratio=0.8):
    split = int(len(X) * ratio)

    X_train = X.iloc[:split]
    X_test = X.iloc[split:]

    y_train = y.iloc[:split]
    y_test = y.iloc[split:]

    return X_train, X_test, y_train, y_test