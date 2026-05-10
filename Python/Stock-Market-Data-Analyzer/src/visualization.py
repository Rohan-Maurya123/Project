# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go


def stock_price_chart(df, ticker):

    plt.figure(figsize=(12, 6))

    plt.plot(df["Date"], df["Close"])

    plt.title(f"{ticker} Stock Price")

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.savefig(f"outputs/charts/{ticker}_price.png")

    plt.close()


def moving_average_chart(df, ticker):

    plt.figure(figsize=(12, 6))

    plt.plot(df["Date"], df["Close"], label="Close Price")

    plt.plot(df["Date"], df["MA_Short"], label="20 MA")

    plt.plot(df["Date"], df["MA_Long"], label="50 MA")

    plt.legend()

    plt.title(f"{ticker} Moving Averages")

    plt.savefig(f"outputs/charts/{ticker}_ma.png")

    plt.close()


def return_distribution(df, ticker):

    plt.figure(figsize=(10, 5))

    sns.histplot(df["Daily_Return"].dropna(), bins=50)

    plt.title("Return Distribution")

    plt.savefig(f"outputs/charts/{ticker}_returns.png")

    plt.close()


def interactive_candlestick(df, ticker):

    fig = go.Figure(data=[go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )])

    fig.update_layout(
        title=f"{ticker} Candlestick Chart"
    )

    fig.write_html(f"outputs/charts/{ticker}_candlestick.html")