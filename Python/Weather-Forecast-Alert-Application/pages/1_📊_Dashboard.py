import streamlit as st
from src.api.weather_api import fetch_weather
from src.alerts.alert_engine import generate_alerts
from src.visualization.charts import (
    create_bar_chart,
    create_pie_chart,
    create_gauge_chart
)
from src.reports.report_generator import save_report

st.set_page_config(layout="wide")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🌦 Real-Time Weather Dashboard")

st.sidebar.header("Weather Search")

city = st.sidebar.text_input("Enter City", "Delhi")

if st.sidebar.button("Fetch Weather"):

    data = fetch_weather(city)

    if data:

        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]
        condition = data["current"]["condition"]["text"]

        country = data["location"]["country"]
        localtime = data["location"]["localtime"]

        alerts = generate_alerts(
            temp,
            humidity,
            condition,
            wind
        )

        st.subheader(f"📍 {city}, {country}")

        st.write(f"🕒 Local Time: {localtime}")

        col1, col2, col3 = st.columns(3)

        col1.metric("🌡 Temperature", f"{temp} °C")
        col2.metric("💧 Humidity", f"{humidity}%")
        col3.metric("🌪 Wind Speed", f"{wind} kph")

        st.success(f"🌤 Condition: {condition}")

        for alert in alerts:
            st.warning(alert)

        chart1, chart2 = st.columns(2)

        with chart1:
            st.plotly_chart(
                create_bar_chart(temp, humidity, wind),
                use_container_width=True
            )

        with chart2:
            st.plotly_chart(
                create_pie_chart(temp, humidity, wind),
                use_container_width=True
            )

        st.plotly_chart(
            create_gauge_chart(temp),
            use_container_width=True
        )

        save_report(
            city,
            temp,
            humidity,
            condition,
            wind,
            alerts
        )

        st.success("✅ Report Saved Successfully")

    else:
        st.error("❌ Failed To Fetch Weather Data")