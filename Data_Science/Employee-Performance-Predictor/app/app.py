import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Add the project root to sys.path to import from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.preprocessing import preprocess_data

# Set page config
st.set_page_config(page_title="Employee Performance Predictor", layout="wide")

# Custom CSS for styling
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
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Load model and encoders
@st.cache_resource
def load_assets():
    try:
        # Adjusted path to work from app/ directory
        model_path = os.path.join(os.path.dirname(__file__), "../models/model.pkl")
        assets = joblib.load(model_path)
        return assets["model"], assets["encoders"]
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None

model, encoders = load_assets()

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "Insights", "EDA"])

if page == "Home":
    st.title("🚀 Employee Performance Predictor")
    st.markdown("""
        Welcome to the **Employee Performance Predictor**! This tool uses machine learning to predict 
        employee performance levels based on various professional and behavioral metrics.
        
        ### Key Features:
        - **Data-Driven Predictions**: Uses a trained Random Forest model.
        - **Business Insights**: Understand which factors drive performance.
        - **Visual EDA**: Explore the trends in your workforce.
        
        ### How to use:
        Navigate to the **Prediction** tab to input employee data and get a performance estimate.
    """)
    st.image("https://images.unsplash.com/photo-1551836022-d5d88e9218df?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", width='stretch')

elif page == "Prediction":
    st.title("🎯 Performance Prediction")
    
    if model is None:
        st.error("Model not found. Please run main.py first to train the model.")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Professional Metrics")
            age = st.slider("Age", 20, 65, 30)
            experience = st.slider("Experience (Years)", 0, 40, 5)
            salary = st.number_input("Annual Salary ($)", min_value=20000, max_value=200000, value=50000)
            department = st.selectbox("Department", ["IT", "HR", "Sales", "Marketing", "Finance"])
            
        with col2:
            st.subheader("Performance Metrics")
            training = st.slider("Training Hours", 0, 150, 40)
            projects = st.slider("Projects Handled", 0, 20, 4)
            attendance = st.slider("Attendance (%)", 60, 100, 95)
            feedback = st.slider("Feedback Score (1-10)", 1, 10, 7)

        if st.button("Predict Performance"):
            # Create a dataframe for the input
            input_df = pd.DataFrame({
                "Age": [age],
                "Experience": [experience],
                "Salary": [salary],
                "Training_Hours": [training],
                "Projects": [projects],
                "Attendance": [attendance],
                "Feedback_Score": [feedback],
                "Department": [department]
            })
            
            # Preprocess the input
            try:
                X_processed = preprocess_data(input_df, is_training=False, encoders=encoders)
                
                # Prediction
                prediction_prob = model.predict_proba(X_processed)[0]
                prediction = model.predict(X_processed)[0]
                
                labels = {0: "Low", 1: "Medium", 2: "High"}
                colors = {"Low": "#dc3545", "Medium": "#ffc107", "High": "#28a745"}
                
                st.markdown(f"""
                    <div class="prediction-card">
                        <h3>Predicted Performance Level:</h3>
                        <h1 style="color: {colors[labels[prediction]]};">{labels[prediction]}</h1>
                    </div>
                """, unsafe_allow_html=True)
                
                # Show probabilities
                st.subheader("Prediction Confidence")
                prob_df = pd.DataFrame({
                    'Performance': ["Low", "Medium", "High"],
                    'Probability': prediction_prob
                })
                st.bar_chart(prob_df.set_index('Performance'))
                
            except Exception as e:
                st.error(f"Prediction Error: {e}")

elif page == "Insights":
    st.title("💡 Business Insights")
    
    if model is not None:
        st.subheader("Feature Importance")
        st.write("These factors have the highest impact on employee performance according to the model:")
        
        # Get feature importance
        # Note: We need to know the features used during training
        # Since we use preprocess_data, let's assume standard features
        importances = model.feature_importances_
        # Need to know feature names after preprocessing
        # For simplicity, let's just show them if they are available
        features = ["Age", "Experience", "Salary", "Training_Hours", "Projects", "Attendance", "Feedback_Score", "Department", "Projects_Per_Year", "Training_Intensity"]
        
        if len(importances) == len(features):
            feat_imp = pd.DataFrame({'Feature': features, 'Importance': importances}).sort_values(by='Importance', ascending=False)
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(data=feat_imp, x='Importance', y='Feature', palette='viridis', ax=ax)
            st.pyplot(fig)
        else:
            st.warning("Feature importance could not be mapped correctly. Showing raw values.")
            st.write(importances)
    else:
        st.info("Train the model first to see insights.")

elif page == "EDA":
    st.title("📊 Exploratory Data Analysis")
    
    if os.path.exists("../data/dataset.csv"):
        data = pd.read_csv("../data/dataset.csv")
        
        st.subheader("Workforce Overview")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Employees", len(data))
        col2.metric("Avg Experience", f"{data['Experience'].mean():.1f} yrs")
        col3.metric("Avg Feedback", f"{data['Feedback_Score'].mean():.1f}/10")
        
        st.subheader("Performance Distribution by Department")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(data=data, x='Department', hue='Performance', ax=ax)
        st.pyplot(fig)
        
        st.subheader("Salary vs Experience (Colored by Performance)")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=data, x='Experience', y='Salary', hue='Performance', palette='coolwarm', ax=ax)
        st.pyplot(fig)
    else:
        st.info("Dataset not found. Please run main.py first.")

st.sidebar.markdown("---")
st.sidebar.info("Empowering smarter HR decisions with data-driven intelligence.")
