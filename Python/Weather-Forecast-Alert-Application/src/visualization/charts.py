import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_bar_chart(temp, humidity, wind):

    df = pd.DataFrame({
        "Metric": ["Temperature", "Humidity", "Wind Speed"],
        "Value": [temp, humidity, wind]
    })

    fig = px.bar(
        df,
        x="Metric",
        y="Value",
        text="Value",
        title="Weather Metrics Overview",
        template="plotly_dark"
    )

    fig.update_layout(height=500)

    return fig


def create_pie_chart(temp, humidity, wind):

    df = pd.DataFrame({
        "Metric": ["Temperature", "Humidity", "Wind Speed"],
        "Value": [temp, humidity, wind]
    })

    fig = px.pie(
        df,
        names="Metric",
        values="Value",
        title="Weather Distribution",
        hole=0.4,
        template="plotly_dark"
    )

    return fig


def create_gauge_chart(temp):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=temp,
        title={'text': "Temperature Gauge"},
        gauge={
            'axis': {'range': [0, 50]},
            'bar': {'color': "cyan"},
            'steps': [
                {'range': [0, 20], 'color': "green"},
                {'range': [20, 35], 'color': "yellow"},
                {'range': [35, 50], 'color': "red"}
            ]
        }
    ))

    fig.update_layout(
        template="plotly_dark",
        height=400
    )

    return fig