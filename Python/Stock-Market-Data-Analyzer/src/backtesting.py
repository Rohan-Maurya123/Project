# src/backtesting.py

def simple_moving_average_strategy(df):

    signals = []

    for i in range(len(df)):

        if df["MA_Short"].iloc[i] > df["MA_Long"].iloc[i]:
            signals.append("BUY")

        elif df["MA_Short"].iloc[i] < df["MA_Long"].iloc[i]:
            signals.append("SELL")

        else:
            signals.append("HOLD")

    df["Signal"] = signals

    return df