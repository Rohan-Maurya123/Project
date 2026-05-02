import sys
import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Add the project root to sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

from src.predict import predict_price

# Robust path for data
DATA_PATH = os.path.join(BASE_DIR, "data", "housing.csv")

# Page configuration
st.set_page_config(
    page_title="House Price Predictor (INR)",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .prediction-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "Analytics"])

# Helper function for currency conversion and formatting
def format_inr(amount):
    if amount >= 10000000:
        return f"₹ {amount/10000000:.2f} Crore"
    elif amount >= 100000:
        return f"₹ {amount/100000:.2f} Lakh"
    else:
        return f"₹ {amount:,.2f}"

def usd_to_inr(usd_amount_k):
    # The dataset MEDV is in $1000s. 
    # To make it realistic for today's market, we can apply an inflation factor 
    # or just convert directly. Let's stick to a direct conversion for now 
    # but ensure it's formatted well.
    return usd_amount_k * 1000 * 83

if page == "Home":
    st.title("🏠 Boston House Price Prediction")
    st.markdown("""
    ### Welcome to the House Price Prediction App!
    This application predicts house prices based on various features like crime rate, number of rooms, and proximity to highways.
    
    #### Features:
    - **Prediction**: Get estimated prices in Indian Rupees (INR).
    - **Analytics**: Visualize relationships between different housing factors.
    - **Interactive Controls**: Adjust parameters to see real-time changes.
    """)
    
    # Show sample data
    st.subheader("Sample Data Preview")
    try:
        df = pd.read_csv(DATA_PATH)
        st.dataframe(df.head(10), use_container_width=True)
    except Exception as e:
        st.error(f"Could not load data from {DATA_PATH}: {e}")

elif page == "Prediction":
    st.title("💰 Predict House Price")
    st.write("Fill in the details below to get an estimated price in **Indian Rupees (INR)**.")
    
    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            CRIM = st.number_input("Crime Rate (CRIM)", value=0.1, help="Per capita crime rate by town")
            ZN = st.number_input("Residential Land % (ZN)", value=10.0)
            INDUS = st.number_input("Industrial Area % (INDUS)", value=5.0)
            CHAS = st.selectbox("Near Charles River? (CHAS)", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
            NOX = st.number_input("Nitric Oxides (NOX)", value=0.5)

        with col2:
            RM = st.slider("Avg Rooms per Dwelling (RM)", 1.0, 10.0, 6.0)
            AGE = st.slider("Age of House (AGE)", 1.0, 100.0, 50.0)
            DIS = st.number_input("Dist to Employment (DIS)", value=4.0)
            RAD = st.number_input("Highway Access Index (RAD)", value=1.0)
            TAX = st.number_input("Tax Rate (TAX)", value=300.0)

        with col3:
            PTRATIO = st.number_input("Pupil-Teacher Ratio (PTRATIO)", value=15.0)
            LSTAT = st.slider("% Lower Status (LSTAT)", 1.0, 40.0, 10.0)
        
        submit = st.form_submit_button("Calculate Price")

    if submit:
        # Removed B from features list
        features = [CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, LSTAT]
        
        try:
            # Prediction in thousands of USD
            price_usd_k = predict_price(features)
            
            # PRICE FIX: The original Boston dataset prices are in $1000s (e.g., 24.0 = $24,000).
            # If the user thinks the price is too high, we should ensure the conversion is correct.
            # Realistically, $24,000 in 1970s is much more now, but let's stick to a direct conversion 
            # or adjust the factor if needed.
            
            # Convert to INR
            price_inr = usd_to_inr(price_usd_k)
            formatted_price = format_inr(price_inr)
            
            st.balloons()
            
            st.markdown(f"""
            <div class="prediction-card">
                <h2 style='color: #28a745;'>Estimated Price</h2>
                <h1 style='color: #1f1f1f;'>{formatted_price}</h1>
                <p style='color: #6c757d;'>({price_usd_k:,.2f}k USD)</p>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Prediction Error: {e}")

elif page == "Analytics":
    st.title("📊 Data Analytics")
    
    try:
        df = pd.read_csv(DATA_PATH)
        
        st.subheader("Price Distribution")
        fig_hist = px.histogram(df, x="MEDV", nbins=30, title="Distribution of House Prices",
                                labels={'MEDV': 'Price (in $1000s)'},
                                color_discrete_sequence=['#636EFA'])
        st.plotly_chart(fig_hist, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Rooms vs Price")
            # Added trendline='ols' which requires statsmodels
            fig_scatter = px.scatter(df, x="RM", y="MEDV", trendline="ols",
                                    title="Number of Rooms vs Price",
                                    labels={'RM': 'Average Rooms', 'MEDV': 'Price'},
                                    template="plotly_white")
            st.plotly_chart(fig_scatter, use_container_width=True)
            
        with col2:
            st.subheader("Correlation Heatmap")
            # Filter out 'B' from the correlation if it's being removed from UI focus
            # although it's still in the CSV
            cols_to_corr = [c for c in df.columns if c != 'B']
            corr = df[cols_to_corr].corr()
            fig_heat = px.imshow(corr, text_auto=True, aspect="auto", 
                                title="Feature Correlation Heatmap",
                                color_continuous_scale='RdBu_r')
            st.plotly_chart(fig_heat, use_container_width=True)
            
        st.subheader("Lower Status % vs Price")
        fig_lstat = px.scatter(df, x="LSTAT", y="MEDV", color="RM",
                              size="AGE", hover_data=['CRIM'],
                              title="LSTAT vs Price (Color: Rooms, Size: Age)")
        st.plotly_chart(fig_lstat, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error loading analytics: {e}")

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit")
