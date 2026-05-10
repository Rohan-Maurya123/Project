# dashboard/app.py

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Stock Market Dashboard",
    layout="wide"
)

# ---------------- TITLE ---------------- #

st.title("📈 Stock Market Data Analyzer Dashboard")

st.markdown("---")

# ---------------- SIDEBAR ---------------- #

st.sidebar.header("Stock Selection")

ticker = st.sidebar.text_input(
    "Enter Stock Ticker",
    value="AAPL"
)

start_date = st.sidebar.date_input(
    "Start Date",
    value=date(2023, 1, 1)
)

end_date = st.sidebar.date_input(
    "End Date",
    value=date.today()
)

# ---------------- FETCH DATA ---------------- #

try:

    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=True
    )

    # Reset index
    df.reset_index(inplace=True)

    # Handle MultiIndex columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Check if dataframe empty
    if df.empty:

        st.error("❌ No stock data found. Try another ticker.")

    else:

        # ---------------- RAW DATA ---------------- #

        st.subheader("📊 Raw Stock Data")

        st.dataframe(df.tail())

        st.markdown("---")

        # ---------------- KPIs ---------------- #

        current_price = float(df["Close"].iloc[-1])

        highest_price = float(df["High"].max())

        lowest_price = float(df["Low"].min())

        avg_volume = float(df["Volume"].mean())

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Current Price",
            f"${current_price:.2f}"
        )

        col2.metric(
            "Highest Price",
            f"${highest_price:.2f}"
        )

        col3.metric(
            "Lowest Price",
            f"${lowest_price:.2f}"
        )

        col4.metric(
            "Average Volume",
            f"{avg_volume:,.0f}"
        )

        st.markdown("---")

        # ---------------- MOVING AVERAGES ---------------- #

        df["MA20"] = df["Close"].rolling(20).mean()

        df["MA50"] = df["Close"].rolling(50).mean()

        # ---------------- PRICE CHART ---------------- #

        st.subheader("📈 Price Trend Analysis")

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=df["Date"],
            y=df["Close"],
            mode='lines',
            name="Close Price"
        ))

        fig.add_trace(go.Scatter(
            x=df["Date"],
            y=df["MA20"],
            mode='lines',
            name="20-Day MA"
        ))

        fig.add_trace(go.Scatter(
            x=df["Date"],
            y=df["MA50"],
            mode='lines',
            name="50-Day MA"
        ))

        fig.update_layout(
            height=600,
            xaxis_title="Date",
            yaxis_title="Price",
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")

        # ---------------- CANDLESTICK ---------------- #

        st.subheader("🕯️ Candlestick Chart")

        candle = go.Figure(data=[go.Candlestick(
            x=df["Date"],
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"]
        )])

        candle.update_layout(
            height=600,
            template="plotly_dark"
        )

        st.plotly_chart(
            candle,
            use_container_width=True
        )

        st.markdown("---")

        # ---------------- DAILY RETURNS ---------------- #

        st.subheader("📉 Daily Returns Distribution")

        df["Daily_Return"] = df["Close"].pct_change()

        returns_fig = px.histogram(
            df,
            x="Daily_Return",
            nbins=50,
            title="Return Distribution"
        )

        returns_fig.update_layout(
            template="plotly_dark",
            height=500
        )

        st.plotly_chart(
            returns_fig,
            use_container_width=True
        )

        st.markdown("---")

        # ---------------- VOLUME ANALYSIS ---------------- #

        st.subheader("📦 Trading Volume Analysis")

        volume_fig = px.bar(
            df,
            x="Date",
            y="Volume",
            title="Volume Analysis"
        )

        volume_fig.update_layout(
            template="plotly_dark",
            height=500
        )

        st.plotly_chart(
            volume_fig,
            use_container_width=True
        )

        st.markdown("---")

        # ---------------- VOLATILITY ---------------- #

        st.subheader("⚠️ Risk Analysis")

        volatility = df["Daily_Return"].std() * (252 ** 0.5)

        st.metric(
            "Annual Volatility",
            f"{volatility:.4f}"
        )

        # ---------------- SIGNAL ---------------- #

        st.subheader("📌 Trend Signal")

        latest_ma20 = df["MA20"].iloc[-1]

        latest_ma50 = df["MA50"].iloc[-1]

        if latest_ma20 > latest_ma50:

            st.success("📈 Bullish Trend Detected")

        elif latest_ma20 < latest_ma50:

            st.error("📉 Bearish Trend Detected")

        else:

            st.warning("⚖️ Sideways Market")

        st.markdown("---")

        st.success("✅ Analysis Completed Successfully")

except Exception as e:

    st.error(f"Error: {e}")