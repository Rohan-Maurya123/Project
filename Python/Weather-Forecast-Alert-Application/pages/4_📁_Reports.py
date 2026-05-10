import streamlit as st
import pandas as pd

st.title("📁 Weather Reports")

try:

    df = pd.read_csv("outputs/forecast_report.csv")

    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name='weather_report.csv',
        mime='text/csv'
    )

except:
    st.error("No Reports Found")