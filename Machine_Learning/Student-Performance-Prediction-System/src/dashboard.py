import streamlit as st
import pandas as pd
import joblib
import os
import plotly.express as px
import plotly.graph_objects as go
import requests
import time

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .main {
        animation: fadeIn 1s ease-in;
    }
    .stButton>button {
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Load artifacts
@st.cache_resource
def load_artifacts():
    model = joblib.load(os.path.join('models', 'student_model.pkl'))
    scaler = joblib.load(os.path.join('models', 'scaler.pkl'))
    feature_names = joblib.load(os.path.join('models', 'feature_names.pkl'))
    label_mappings = joblib.load(os.path.join('models', 'label_mappings.pkl'))
    return model, scaler, feature_names, label_mappings

try:
    model, scaler, feature_names, label_mappings = load_artifacts()
except Exception as e:
    st.error(f"Error loading model artifacts: {e}. Please run 'python src/train.py' first.")

def main():
    st.title("🎓 Student Performance Prediction System")
    st.markdown("""
    Predicting academic success and identifying at-risk students using Machine Learning.
    """)

    tabs = st.tabs(["📊 Analytics Dashboard", "🔮 Prediction Tool", "ℹ️ About Project"])

    # --- TAB 1: Analytics ---
    with tabs[0]:
        st.header("Exploratory Data Analysis")
        df = pd.read_csv(os.path.join('data', 'student-mat.csv'), sep=';')
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Distribution of Final Grades (G3)")
            fig_hist = px.histogram(df, x="G3", nbins=20, marginal="box", 
                                  title="Final Grade Distribution",
                                  color_discrete_sequence=['#636EFA'])
            fig_hist.update_layout(height=400)
            st.plotly_chart(fig_hist, use_container_width=True)
            
        with col2:
            st.subheader("Study Time vs Final Grade")
            fig_box = px.box(df, x="studytime", y="G3", 
                           title="Impact of Study Time on Grades",
                           color="studytime",
                           labels={"studytime": "Weekly Study Time (1-4)", "G3": "Final Grade (0-20)"})
            fig_box.update_layout(height=400)
            st.plotly_chart(fig_box, use_container_width=True)
            
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Social Habits & Performance")
            fig_scatter = px.scatter(df, x="absences", y="G3", color="goout", size="age",
                                   hover_data=['sex', 'health'],
                                   title="Absences vs Grades (sized by Age, colored by Socializing)")
            fig_scatter.update_layout(height=400)
            st.plotly_chart(fig_scatter, use_container_width=True)
            
        with col4:
            st.subheader("Family Support vs Grade Band")
            df['grade_band'] = df['G3'].apply(lambda x: 'Pass' if x >= 10 else 'Fail')
            fig_pie = px.sunburst(df, path=['grade_band', 'famsup', 'sex'], values='G3',
                                title="Performance Breakdown by Support and Gender")
            fig_pie.update_layout(height=400)
            st.plotly_chart(fig_pie, use_container_width=True)

    # --- TAB 2: Prediction ---
    with tabs[1]:
        st.header("Student Risk Assessment")
        
        with st.form("prediction_form"):
            st.subheader("📝 Enter Student Profile")
            c1, c2, c3 = st.columns(3)
            
            with c1:
                school = st.selectbox("School", ["GP", "MS"], help="GP: Gabriel Pereira, MS: Mousinho da Silveira")
                sex = st.selectbox("Sex", ["F", "M"])
                age = st.slider("Age", 15, 22, 18)
                address = st.selectbox("Address Type", ["U", "R"], help="U: Urban, R: Rural")
                famsize = st.selectbox("Family Size", ["GT3", "LE3"], help="GT3: >3, LE3: <=3")
                pstatus = st.selectbox("Parent Status", ["T", "A"], help="T: Together, A: Apart")
                medu = st.select_slider("Mother's Education", options=[0, 1, 2, 3, 4], help="0: None, 4: Higher")
                fedu = st.select_slider("Father's Education", options=[0, 1, 2, 3, 4])
                mjob = st.selectbox("Mother's Job", ["teacher", "health", "services", "at_home", "other"])
                fjob = st.selectbox("Father's Job", ["teacher", "health", "services", "at_home", "other"])

            with c2:
                reason = st.selectbox("School Choice Reason", ["home", "reputation", "course", "other"])
                guardian = st.selectbox("Guardian", ["mother", "father", "other"])
                traveltime = st.slider("Travel Time (1-4)", 1, 4, 1, help="1: <15m, 4: >1h")
                studytime = st.slider("Study Time (1-4)", 1, 4, 2, help="1: <2h, 4: >10h")
                failures = st.slider("Past Failures", 0, 3, 0)
                schoolsup = st.radio("School Support", ["yes", "no"], horizontal=True)
                famsup = st.radio("Family Support", ["yes", "no"], horizontal=True)
                paid = st.radio("Paid Classes", ["yes", "no"], horizontal=True)
                activities = st.radio("Activities", ["yes", "no"], horizontal=True)
                nursery = st.radio("Nursery", ["yes", "no"], horizontal=True)

            with c3:
                higher = st.radio("Higher Ed Desire", ["yes", "no"], horizontal=True)
                internet = st.radio("Internet", ["yes", "no"], horizontal=True)
                romantic = st.radio("Romantic", ["yes", "no"], horizontal=True)
                famrel = st.slider("Family Quality (1-5)", 1, 5, 4)
                freetime = st.slider("Free Time (1-5)", 1, 5, 3)
                goout = st.slider("Going Out (1-5)", 1, 5, 3)
                dalc = st.slider("Workday Alcohol (1-5)", 1, 5, 1)
                walc = st.slider("Weekend Alcohol (1-5)", 1, 5, 1)
                health = st.slider("Health Status (1-5)", 1, 5, 5)
                absences = st.number_input("Absences", 0, 100, 0)

            st.markdown("<br>", unsafe_allow_html=True)
            submit = st.form_submit_button("🚀 Run Prediction Analysis")

        if submit:
            with st.spinner("Analyzing student profile..."):
                time.sleep(1) # Visual effect
                
                # Prepare input data
                input_dict = {
                    'school': school, 'sex': sex, 'age': age, 'address': address,
                    'famsize': famsize, 'Pstatus': pstatus, 'Medu': medu, 'Fedu': fedu,
                    'Mjob': mjob, 'Fjob': fjob, 'reason': reason, 'guardian': guardian,
                    'traveltime': traveltime, 'studytime': studytime, 'failures': failures,
                    'schoolsup': schoolsup, 'famsup': famsup, 'paid': paid,
                    'activities': activities, 'nursery': nursery, 'higher': higher,
                    'internet': internet, 'romantic': romantic, 'famrel': famrel,
                    'freetime': freetime, 'goout': goout, 'Dalc': dalc, 'Walc': walc,
                    'health': health, 'absences': absences
                }
                
                input_df = pd.DataFrame([input_dict])
                
                # Preprocess
                for col, mapping in label_mappings.items():
                    if col in input_df.columns:
                        input_df[col] = input_df[col].map(mapping).fillna(0)
                
                input_df = input_df[feature_names]
                input_scaled = scaler.transform(input_df)
                
                # Predict
                prediction = model.predict(input_scaled)
                probs = model.predict_proba(input_scaled)[0]
                
                st.divider()
                st.header("🔍 Prediction Results")
                
                res_col1, res_col2 = st.columns([1, 1])
                
                with res_col1:
                    if prediction[0] == 1:
                        st.balloons()
                        st.success("### Prediction: **PASS** ✅")
                        color = "green"
                    else:
                        st.error("### Prediction: **FAIL** ❌")
                        color = "red"
                    
                    # Gauge chart for confidence
                    confidence = probs[1] if prediction[0] == 1 else probs[0]
                    fig_gauge = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = confidence * 100,
                        title = {'text': "Confidence Level (%)"},
                        gauge = {
                            'axis': {'range': [0, 100]},
                            'bar': {'color': color},
                            'steps': [
                                {'range': [0, 50], 'color': "lightgray"},
                                {'range': [50, 80], 'color': "gray"},
                                {'range': [80, 100], 'color': "darkgray"}
                            ]
                        }
                    ))
                    fig_gauge.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
                    st.plotly_chart(fig_gauge, use_container_width=True)

                with res_col2:
                    st.subheader("Student Profile Radar")
                    # Normalized Radar Chart
                    radar_data = pd.DataFrame(dict(
                        r=[studytime, famrel, freetime, goout, health],
                        theta=['Study Time', 'Family Rel', 'Free Time', 'Go Out', 'Health']
                    ))
                    fig_radar = px.line_polar(radar_data, r='r', theta='theta', line_close=True)
                    fig_radar.update_traces(fill='toself')
                    fig_radar.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
                    st.plotly_chart(fig_radar, use_container_width=True)

                if prediction[0] == 0:
                    st.warning("⚠️ **Intervention Strategy:** This student is flagged as high-risk. We recommend immediate academic counseling and parental engagement to address potential social or study habit issues.")
                else:
                    st.info("💡 **Observation:** Student is performing well. Maintain current study habits and engagement levels.")

    # --- TAB 3: About ---
    with tabs[2]:
        st.header("Project Documentation")
        st.markdown("""
        ### Student Performance Prediction System (v1.0)
        
        #### 🏗️ Architecture
        - **Preprocessing**: Feature engineering and standardization using Scikit-Learn.
        - **Model**: Random Forest Classifier (100 estimators) trained on 395 student records.
        - **Interface**: Streamlit with Plotly integration for responsive data visualization.
        
        #### 📊 Key Features
        - **Real-time Inference**: Get instant results for any student profile.
        - **Interactive EDA**: Explore data trends through sunburst, histogram, and box plots.
        - **Risk Profiling**: Automatic identification of academic risk factors.
        
        #### 🧪 Simulation Guide
        Try these scenarios in the Prediction Tool:
        1. **Low Study Time + High Absences** -> Usually predicts **Fail**.
        2. **High Study Time + Family Support** -> Usually predicts **Pass**.
        3. **High Alcohol Consumption** -> Significant impact on prediction risk.
        """)

if __name__ == "__main__":
    main()
