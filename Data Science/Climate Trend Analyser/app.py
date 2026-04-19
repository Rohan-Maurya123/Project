import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
from src.data_loader import load_data
from src.preprocessing import clean_data
from src.anomaly_detection import detect_anomalies
from src.trend_analysis import trend_analysis
from src.forecasting import forecast_temp

# Page Configuration
st.set_page_config(
    page_title="Climate Trend Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a professional dark look
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }
    
    /* Metric Card styling */
    div[data-testid="stMetric"] {
        background-color: #1c2128;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        transition: transform 0.2s ease-in-out;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        border-color: #58a6ff;
    }
    
    /* Text colors */
    [data-testid="stMetricValue"] {
        color: #58a6ff !important;
        font-weight: 700 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #adbac7 !important;
        font-size: 0.9rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Global text and sidebar text */
    .stMarkdown, p, span, label {
        color: #adbac7 !important;
    }
    
    /* Ensure headers are bright white */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar specific text */
    section[data-testid="stSidebar"] .stMarkdown p, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] .stCaption {
        color: #ffffff !important;
    }

    /* Input widgets text color */
    .stSelectbox div, .stNumberInput div, .stTextInput div, .stDateInput div {
        color: #ffffff !important;
    }
    
    /* Caption styling */
    .stCaption {
        color: #8b949e !important;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #238636;
        color: white;
        border-radius: 6px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #2ea043;
        border: none;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Data Loading Logic
data_path = "data/climate_data.csv"

if not os.path.exists(data_path) or os.path.getsize(data_path) == 0:
    st.info("🔄 Generating initial synthetic dataset...")
    from src.data_simulation import generate_climate_data
    generate_climate_data()

@st.cache_data
def get_data():
    raw_df = load_data(data_path)
    return clean_data(raw_df)

df = get_data()

# Sidebar UI
st.sidebar.title("🌍 Climate Dashboard")
st.sidebar.markdown("---")

st.sidebar.subheader("📅 Data Filters")
min_date = df['Date'].min().to_pydatetime()
max_date = df['Date'].max().to_pydatetime()
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

st.sidebar.subheader("⚙️ Analysis Settings")
show_trend = st.sidebar.checkbox("Show Trend Line (Rolling Mean)", value=True)
show_anomalies = st.sidebar.checkbox("Highlight Anomalies", value=True)
anomaly_threshold = st.sidebar.slider("Anomaly Sensitivity", 1.0, 4.0, 2.0)

st.sidebar.markdown("---")
st.sidebar.info("This dashboard provides real-time climate trend analysis, anomaly detection, and predictive forecasting.")

# Filter Data
if len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    filtered_df = df.loc[mask].copy()
else:
    filtered_df = df.copy()

# Header Section
st.title("🌍 Climate Trend Intelligence")
st.markdown(f"**Analyzing climate patterns from {filtered_df['Date'].min().strftime('%Y-%m-%d')} to {filtered_df['Date'].max().strftime('%Y-%m-%d')}**")

# Performance Metrics
m1, m2, m3, m4 = st.columns(4)

avg_temp = filtered_df['Temperature'].mean()
max_temp = filtered_df['Temperature'].max()
min_temp = filtered_df['Temperature'].min()

# Run Anomaly Detection for metrics
filtered_df = detect_anomalies(filtered_df, threshold=anomaly_threshold)
anomaly_count = filtered_df['Anomaly'].sum()

m1.metric("Average Temperature", f"{avg_temp:.2f} °C")
m2.metric("Maximum Temperature", f"{max_temp:.2f} °C")
m3.metric("Minimum Temperature", f"{min_temp:.2f} °C")
m4.metric("Anomalies Detected", int(anomaly_count), delta_color="inverse")

# Main Visualization
st.subheader("📈 Temperature Trend Analysis")

# Add Trend Analysis
if show_trend:
    filtered_df = trend_analysis(filtered_df)

# Create Plotly Figure
fig = go.Figure()

# Base Temperature Line
fig.add_trace(go.Scatter(
    x=filtered_df['Date'], 
    y=filtered_df['Temperature'],
    name='Observed Temp',
    line=dict(color='#3498db', width=2),
    opacity=0.7
))

# Trend Line
if show_trend:
    fig.add_trace(go.Scatter(
        x=filtered_df['Date'], 
        y=filtered_df['Rolling_Mean'],
        name='12-Period Trend',
        line=dict(color='#e67e22', width=3, dash='dash')
    ))

# Anomalies
if show_anomalies:
    anomalies = filtered_df[filtered_df['Anomaly'] == 1]
    fig.add_trace(go.Scatter(
        x=anomalies['Date'], 
        y=anomalies['Temperature'],
        mode='markers',
        name='Anomalies',
        marker=dict(color='#e74c3c', size=10, symbol='x')
    ))

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    hovermode="x unified",
    xaxis=dict(title=dict(font=dict(color='white')), tickfont=dict(color='white')),
    yaxis=dict(title=dict(font=dict(color='white')), tickfont=dict(color='white')),
    legend=dict(
        font=dict(color='white'),
        orientation="h", 
        yanchor="bottom", 
        y=1.02, 
        xanchor="right", 
        x=1
    )
)

st.plotly_chart(fig, use_container_width=True)

# Forecasting Section
st.markdown("---")
c1, c2 = st.columns([2, 1])

with c1:
    st.subheader("🔮 30-Day Predictive Forecast")
    forecast_df = forecast_temp(df) # Forecast based on full data for better context
    
    fig_forecast = px.line(
        forecast_df, x='Date', y='Forecast',
        title="Future Temperature Projections (ARIMA)",
        labels={'Forecast': 'Predicted Temp (°C)'}
    )
    fig_forecast.update_traces(line_color='#2ecc71', line_width=3)
    fig_forecast.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(title=dict(font=dict(color='white')), tickfont=dict(color='white')),
        yaxis=dict(title=dict(font=dict(color='white')), tickfont=dict(color='white'))
    )
    st.plotly_chart(fig_forecast, use_container_width=True)

with c2:
    st.subheader("📊 Data Distribution")
    fig_dist = px.histogram(
        filtered_df, x='Temperature', 
        nbins=30, 
        color_discrete_sequence=['#9b59b6'],
        marginal="box"
    )
    fig_dist.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(title=dict(font=dict(color='white')), tickfont=dict(color='white')),
        yaxis=dict(title=dict(font=dict(color='white')), tickfont=dict(color='white'))
    )
    st.plotly_chart(fig_dist, use_container_width=True)

# Raw Data Section
with st.expander("📂 View Raw Dataset & Exports"):
    st.dataframe(filtered_df, use_container_width=True)
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name='climate_analysis_export.csv',
        mime='text/csv',
    )

st.markdown("---")
st.caption("Built with ❤️ using Streamlit, Pandas, and Plotly. | Climate Trend Analyser v2.0")