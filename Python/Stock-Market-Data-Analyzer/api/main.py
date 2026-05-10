# api/main.py

from fastapi import FastAPI
import yfinance as yf

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Stock Market API Running"
    }


@app.get("/stock/{ticker}")
def stock_data(ticker: str):

    df = yf.download(
        ticker,
        period="1mo"
    )

    latest_price = df["Close"].iloc[-1]

    return {
        "ticker": ticker,
        "latest_price": float(latest_price)
    }