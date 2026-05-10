import streamlit as st
from src.api.weather_api import fetch_weather
from src.alerts.alert_engine import generate_alerts
from src.visualization.charts import (
    create_weather_chart,
    create_pie_chart
)
from src.reports.report_generator import save_report

st.set_page_config(
    page_title="Weather Forecast Dashboard",
    page_icon="🌦",
    layout="wide"
)

# --------------------------
# CUSTOM CSS
# --------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: #00BFFF;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# TITLE
# --------------------------

st.title("🌦 Weather Forecast & Alert Dashboard")

st.markdown("---")

# --------------------------
# SIDEBAR
# --------------------------

st.sidebar.header("⚙ Settings")

city = st.sidebar.text_input(
    "Enter City Name",
    "Delhi"
)

fetch_button = st.sidebar.button("🔍 Fetch Weather")

# --------------------------
# MAIN
# --------------------------

if fetch_button:

    data = fetch_weather(city)

    if data:

        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        condition = data["current"]["condition"]["text"]
        wind = data["current"]["wind_kph"]

        country = data["location"]["country"]
        localtime = data["location"]["localtime"]

        alerts = generate_alerts(
            temp,
            humidity,
            condition,
            wind
        )

        # --------------------------
        # WEATHER INFO
        # --------------------------

        st.subheader("📍 Location Information")

        st.write(f"### {city}, {country}")
        st.write(f"🕒 Local Time: {localtime}")

        st.markdown("---")

        # --------------------------
        # METRICS
        # --------------------------

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "🌡 Temperature",
            f"{temp} °C"
        )

        col2.metric(
            "💧 Humidity",
            f"{humidity}%"
        )

        col3.metric(
            "🌪 Wind Speed",
            f"{wind} kph"
        )

        st.markdown("---")

        # --------------------------
        # CONDITION
        # --------------------------

        st.subheader("🌤 Current Weather Condition")

        st.success(condition)

        st.markdown("---")

        # --------------------------
        # ALERTS
        # --------------------------

        st.subheader("🚨 Weather Alerts")

        for alert in alerts:
            st.warning(alert)

        st.markdown("---")

        # --------------------------
        # CHARTS
        # --------------------------

        st.subheader("📊 Weather Analytics")

        chart1, chart2 = st.columns(2)

        with chart1:
            bar_chart = create_weather_chart(
                temp,
                humidity,
                wind
            )

            st.plotly_chart(
                bar_chart,
                use_container_width=True
            )

        with chart2:
            pie_chart = create_pie_chart(
                temp,
                humidity,
                wind
            )

            st.plotly_chart(
                pie_chart,
                use_container_width=True
            )

        # --------------------------
        # SAVE REPORT
        # --------------------------

        save_report(
            city,
            temp,
            humidity,
            condition,
            wind,
            alerts
        )

        st.success(
            "✅ Weather Report Saved in outputs folder"
        )

    else:
        st.error("❌ Failed To Fetch Weather Data")