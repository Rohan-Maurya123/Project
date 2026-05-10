import streamlit as st

st.set_page_config(
    page_title="Weather Forecast Dashboard",
    page_icon="🌦",
    layout="wide"
)

st.title("🌦 Weather Forecast & Alert Application")

st.markdown("""
# Welcome To Professional Weather Dashboard

Use sidebar navigation to open:

- Dashboard
- Alerts
- Analytics
- Reports

This project uses:
- Python
- Streamlit
- Plotly
- WeatherAPI
- Real-time Weather Alerts
""")