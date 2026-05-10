import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Weather Analytics")

try:

    df = pd.read_csv("outputs/forecast_report.csv")

    st.dataframe(df)

    fig = px.line(
        df,
        x="Timestamp",
        y="Temperature (C)",
        title="Temperature Trend",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

except:
    st.warning("No Report Data Available")