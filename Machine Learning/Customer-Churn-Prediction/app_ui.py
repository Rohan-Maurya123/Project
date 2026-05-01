import streamlit as st
import pandas as pd
import joblib
import time

# Set page config for a premium feel
st.set_page_config(
    page_title="Executive Churn Insights",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Custom CSS
st.markdown("""
    <style>
    /* Main background and global text */
    .stApp {
        background-color: #0e1117;
        color: #e0e6ed;
    }

    header, [data-testid="stHeader"] {
        visibility: hidden;
        height: 0px;
        display: none;
    }

    [data-testid="stDecoration"] {
        display: none;
        visibility: hidden;
        height: 0px;
    }

    .main .block-container {
        padding-top: 2rem;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    
    section[data-testid="stSidebar"] .stMarkdown, 
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] li {
        color: #ffffff !important;
        font-size: 1.05rem;
        font-weight: 400;
    }

    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: #e3b341 !important;
    }

    .stSlider label, 
    .stNumberInput label, 
    .stSelectbox label, 
    .stTextInput label,
    .stToggle label,
    div[data-testid="stWidgetLabel"] p {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    div[data-testid="stMetricLabel"] p {
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
    }

    .stCaption {
        color: #a3abb5 !important;
        font-size: 0.9rem !important;
    }
    
    h1, h2, h3 {
        color: #e3b341 !important;
        font-family: 'Playfair Display', serif;
    }
    
    div[data-testid="stMetricValue"] {
        color: #e3b341;
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background-color: #e3b341;
        color: #0e1117;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        background-color: #f0c75e !important;
        color: #0e1117 !important;
        box-shadow: 0 4px 15px rgba(227, 179, 65, 0.4);
        transform: translateY(-2px);
    }
    
    .stNumberInput input, .stSelectbox select {
        background-color: #1c2128 !important;
        color: white !important;
        border: 1px solid #30363d !important;
    }
    
    .result-container {
        background-color: #1c2128;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #e3b341;
        margin-top: 20px;
    }
    
    hr {
        border-top: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# Load assets
@st.cache_resource
def load_assets():
    pipeline = joblib.load("models/churn_pipeline.pkl")
    categories = joblib.load("models/categories.pkl")
    features_list = joblib.load("models/features_list.pkl")
    return pipeline, categories, features_list

try:
    pipeline, categories, features_list = load_assets()
except Exception as e:
    st.error("Assets not found. Please run the training script.")
    st.stop()

# Header
st.title("💎 Executive Churn Intelligence")
st.markdown("---")

# Layout
col_inputs, col_results = st.columns([1.5, 1])

with col_inputs:
    st.subheader("📋 Customer Profile")
    
    # Organize inputs into tabs for better UI
    tab1, tab2, tab3 = st.tabs(["Personal Info", "Service Details", "Billing & Contract"])
    
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            gender = st.selectbox("Gender", categories["gender"])
            senior = st.selectbox("Senior Citizen", [0, 1], help="0: No, 1: Yes")
        with c2:
            partner = st.selectbox("Partner", categories["Partner"])
            dependents = st.selectbox("Dependents", categories["Dependents"])
            
    with tab2:
        c3, c4 = st.columns(2)
        with c3:
            phone = st.selectbox("Phone Service", categories["PhoneService"])
            multiple_lines = st.selectbox("Multiple Lines", categories["MultipleLines"])
            internet = st.selectbox("Internet Service", categories["InternetService"])
            online_security = st.selectbox("Online Security", categories["OnlineSecurity"])
        with c4:
            online_backup = st.selectbox("Online Backup", categories["OnlineBackup"])
            device_protection = st.selectbox("Device Protection", categories["DeviceProtection"])
            tech_support = st.selectbox("Tech Support", categories["TechSupport"])
            streaming_tv = st.selectbox("Streaming TV", categories["StreamingTV"])
            streaming_movies = st.selectbox("Streaming Movies", categories["StreamingMovies"])
            
    with tab3:
        c5, c6 = st.columns(2)
        with c5:
            tenure = st.slider("Tenure (Months)", 0, 72, 12)
            contract = st.selectbox("Contract Type", categories["Contract"])
            paperless = st.selectbox("Paperless Billing", categories["PaperlessBilling"])
        with c6:
            monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 65.0)
            total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 800.0)
            payment_method = st.selectbox("Payment Method", categories["PaymentMethod"])

    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.button("Generate Risk Assessment")

with col_results:
    st.subheader("📊 Analytical Output")
    
    if predict_btn:
        with st.spinner('Performing Deep Analysis...'):
            time.sleep(1.2)
            
            # Map the exact keys used in training
            input_dict = {
                "tenure": tenure,
                "MonthlyCharges": monthly_charges,
                "TotalCharges": total_charges,
                "gender": gender,
                "SeniorCitizen": senior,
                "Partner": partner,
                "Dependents": dependents,
                "PhoneService": phone,
                "MultipleLines": multiple_lines,
                "InternetService": internet,
                "OnlineSecurity": online_security,
                "OnlineBackup": online_backup,
                "DeviceProtection": device_protection,
                "TechSupport": tech_support,
                "StreamingTV": streaming_tv,
                "StreamingMovies": streaming_movies,
                "Contract": contract,
                "PaperlessBilling": paperless,
                "PaymentMethod": payment_method
            }
            
            # Feature Engineering in UI
            service_vals = [phone, multiple_lines, internet, online_security, 
                           online_backup, device_protection, tech_support, 
                           streaming_tv, streaming_movies]
            input_dict["TotalServices"] = sum(1 for v in service_vals if "Yes" in str(v))
            input_dict["AvgMonthlyPerTenure"] = monthly_charges / (tenure + 1)
            
            input_df = pd.DataFrame([input_dict])
            
            # Prediction using Pipeline
            prob = pipeline.predict_proba(input_df)[0][1]
            prediction = pipeline.predict(input_df)[0]
            
            st.markdown('<div class="result-container">', unsafe_allow_html=True)
            
            if prediction == 1:
                st.error("### ⚠ CRITICAL RISK DETECTED")
                st.metric("Churn Probability", f"{prob*100:.1f}%", delta="High Risk", delta_color="inverse")
                st.markdown("---")
                st.write("**Recommended Strategy:**")
                st.info("Immediate intervention required. High probability of departure detected based on current service patterns.")
            else:
                st.success("### ✅ STABLE CUSTOMER")
                st.metric("Churn Probability", f"{prob*100:.1f}%", delta="Low Risk", delta_color="normal")
                st.markdown("---")
                st.write("**Recommended Strategy:**")
                st.balloons()
                st.info("Customer retention is high. Maintain current engagement levels and monitor for service changes.")
            
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Complete the customer profile and click 'Generate Risk Assessment' to view real-time insights.")

# Sidebar info
st.sidebar.title("💎 Intelligence Hub")
st.sidebar.markdown("""
This system uses a **multi-feature XGBoost Pipeline** with automated scaling and encoding for maximum reliability.
""")

st.sidebar.divider()
st.sidebar.subheader("Model Statistics")
st.sidebar.write("🎯 **Reliability:** High (Full Feature Analysis)")
st.sidebar.write("🔍 **Engine:** XGBoost + StandardScaler")
st.sidebar.write("⚖️ **Status:** Operational")

st.sidebar.divider()
st.sidebar.caption("💎 Executive Churn Intelligence v3.0")
