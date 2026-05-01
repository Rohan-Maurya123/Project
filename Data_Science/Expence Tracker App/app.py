import streamlit as st
import pandas as pd
import numpy as np
from src.data_generator import generate_data
from src.data_cleaning import clean_data
from src.analysis import analyze_data, generate_insights
from src.visualization import create_plotly_charts
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="NEURAL EXPENSE CORE",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- FUTURISTIC STYLING ---
st.markdown("""
    <style>
    /* Dark Theme Base */
    .stApp {
        background: radial-gradient(circle at top right, #0a0e14, #000000);
        color: #00f2ff;
    }
    
    /* Neon Metric Cards */
    [data-testid="stMetricValue"] {
        color: #00f2ff !important;
        text-shadow: 0 0 10px #00f2ff;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Cyber Metric Cards with Pulsing Glow */
    .stMetric {
        background: rgba(0, 242, 255, 0.03);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(0, 242, 255, 0.2);
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.05);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .stMetric:hover {
        transform: translateY(-5px);
        border-color: #00f2ff;
        box-shadow: 0 0 25px rgba(0, 242, 255, 0.3);
        background: rgba(0, 242, 255, 0.08);
    }

    /* Scanning Line Animation */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: rgba(0, 242, 255, 0.1);
        z-index: 9999;
        animation: scan 8s linear infinite;
        pointer-events: none;
    }

    @keyframes scan {
        0% { top: 0; }
        100% { top: 100%; }
    }

    /* Cyber Insight Cards with Magenta Glow */
    .insight-card {
        background: rgba(255, 0, 255, 0.03);
        padding: 20px;
        border: 1px solid rgba(255, 0, 255, 0.2);
        border-left: 5px solid #ff00ff;
        border-radius: 10px;
        margin-bottom: 15px;
        color: #e0e0e0;
        font-family: 'Segoe UI', sans-serif;
        box-shadow: 0 0 15px rgba(255, 0, 255, 0.1);
        backdrop-filter: blur(5px);
    }

    /* Styled Dataframe - High Tech Grid */
    .stDataFrame {
        border: 1px solid rgba(0, 242, 255, 0.15);
        border-radius: 12px;
        background: rgba(0, 10, 20, 0.4) !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
    }

    /* Tab HUD Style */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: rgba(0, 242, 255, 0.05);
        border-radius: 5px 5px 0px 0px;
        border: 1px solid rgba(0, 242, 255, 0.1);
        color: #888;
        padding: 0 20px;
    }

    .stTabs [aria-selected="true"] {
        background-color: rgba(0, 242, 255, 0.15) !important;
        border-bottom: 3px solid #00f2ff !important;
        color: #00f2ff !important;
        text-shadow: 0 0 10px #00f2ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("💠 SYSTEM CORE")
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=120)
    
    st.markdown("### DATA SYNC")
    if st.button("⚡ REGENERATE DATASET", use_container_width=True):
        with st.spinner("SYNTHESIZING NEW REALITY..."):
            # Ensure fresh generation
            generate_data()
            clean_data()
            # Clear cache and refresh state
            st.cache_data.clear()
            st.success("NEW DATASTREAM INITIALIZED")
            st.rerun()

    st.divider()
    st.markdown("""
    **SYSTEM STATUS:** `OPERATIONAL`  
    **ENCRYPTION:** `AES-256`  
    **NEURAL LINK:** `ACTIVE`
    """)

# --- LOAD DATA ---
@st.cache_data
def get_data():
    if not os.path.exists("data/cleaned_expenses.csv"):
        generate_data()
        clean_data()
    data = pd.read_csv("data/cleaned_expenses.csv")
    data['Date'] = pd.to_datetime(data['Date'])
    return data

df = get_data()
metrics = analyze_data()

# --- MAIN UI ---
st.title("🔮 NEURAL EXPENSE TRACKER")
st.markdown("---")

# 1. TOP METRICS
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("TOTAL OUTPUT", f"₹{metrics['total_expenses']:,.0f}")
with col2:
    st.metric("CREDIT INPUT", f"₹{metrics['total_income']:,.0f}")
with col3:
    st.metric("RESERVE DELTA", f"₹{metrics['net_savings']:,.0f}", delta=f"{(metrics['net_savings']/metrics['total_income']*100):.1f}%")
with col4:
    st.metric("FLUX DENSITY", f"₹{metrics['avg_daily_spending']:,.0f}")

st.markdown("###")

# 2. TABS FOR ANALYSIS
tab1, tab2, tab3, tab4 = st.tabs(["📊 ANALYTICS CORE", "🗃️ DATA ARCHIVE", "🧠 NEURAL INSIGHTS", "🧪 SIMULATION LOGIC"])

with tab1:
    fig_cat, fig_trend, fig_daily, fig_monthly_bar = create_plotly_charts(df, metrics)
    
    st.markdown("### MONTHLY SECTOR ANALYSIS")
    st.plotly_chart(fig_monthly_bar, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(fig_cat, use_container_width=True)
    with c2:
        st.plotly_chart(fig_trend, use_container_width=True)
    
    st.plotly_chart(fig_daily, use_container_width=True)

with tab2:
    st.subheader("RAW CLEANED DATASTREAM")
    
    # Advanced Styled Table for AI feel
    styled_df = df.copy()
    
    # Add icons to Status/Type
    styled_df['Status'] = styled_df['Type'].apply(lambda x: "🟢 INCOME" if x == "Income" else "🔺 EXPENSE")
    
    # Add emojis to Sector/Category
    cat_icons = {
        "Food": "🍔 Food",
        "Travel": "✈️ Travel",
        "Rent": "🏠 Rent",
        "Bills": "💡 Bills",
        "Shopping": "🛍️ Shopping",
        "Entertainment": "🎬 Entertainment",
        "Salary": "💰 Salary"
    }
    styled_df['Sector'] = styled_df['Category'].map(lambda x: cat_icons.get(x, f"💠 {x}"))
    
    st.dataframe(
        styled_df[['Date', 'Sector', 'Amount', 'Status', 'Description']],
        use_container_width=True,
        hide_index=True,
        column_config={
            "Date": st.column_config.DateColumn("TIMESTAMP", format="YYYY-MM-DD"),
            "Amount": st.column_config.NumberColumn(
                "FLUX VALUE",
                format="₹%d",
            ),
            "Sector": st.column_config.TextColumn("NEURAL SECTOR"),
            "Status": st.column_config.TextColumn("VITAL STATUS"),
            "Description": st.column_config.TextColumn("LOG DETAILS")
        }
    )
    
    st.download_button(
        label="📥 EXPORT DATASET",
        data=df.to_csv(index=False),
        file_name="neural_expenses.csv",
        mime="text/csv"
    )

with tab3:
    st.subheader("NEURAL PROCESSOR OUTPUT")
    insights = generate_insights(metrics)
    for ins in insights:
        st.markdown(f"<div class='insight-card'>⚡ {ins}</div>", unsafe_allow_html=True)

with tab4:
    st.header("🔬 SIMULATION ARCHITECTURE")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("1️⃣ DATA SYNTHESIS")
        st.write("""
        System utilizes a **Stochastic Probabilistic Model**:
        - **Deterministic Nodes**: Rent/Bills anchored to T+0 (1st of Month).
        - **Weekend Amplification**: Scalar 1.5x applied to 'Food' nodes on Sat/Sun.
        - **Entropy Logic**: 15% Shopping / 5% Travel probability per cycle.
        """)
        
    with col_b:
        st.subheader("2️⃣ ANOMALY DETECTION")
        st.write("""
        Heuristic-based **Statistical Thresholding**:
        - **Baseline**: Moving average of daily flux.
        - **Flag Trigger**: Intensity > 1.5x Baseline.
        - Identifies high-energy spending events.
        """)