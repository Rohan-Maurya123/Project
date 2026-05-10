import streamlit as st
import sys
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main_pipeline import process_resumes

# Page Configuration
st.set_page_config(
    page_title="AI Resume Screener Dashboard",
    page_icon="📄",
    layout="wide"
)

# Custom CSS for a modern look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .shortlisted {
        color: #28a745;
        font-weight: bold;
    }
    .rejected {
        color: #dc3545;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙️ Configuration")
resume_folder = st.sidebar.text_input("Resume Folder Path", value="resumes")
threshold = st.sidebar.slider("Shortlisting Threshold (%)", 0, 100, 35)

st.sidebar.markdown("---")
st.sidebar.info("""
**How to use:**
1. Enter the Job Description.
2. Click 'Screen Resumes'.
3. View the analytics dashboard.
4. Download the final report.
""")

# Main Content
st.title("📄 AI-Powered Resume Screening Dashboard")
st.markdown("---")

# Layout for Input
col1, col2 = st.columns([2, 1])

with col1:
    job_description = st.text_area("🎯 Job Description", height=200, placeholder="Paste the job requirements here...")

with col2:
    st.markdown("### 🚀 Actions")
    screen_button = st.button("🔥 Screen Resumes", use_container_width=True)
    if screen_button:
        if not job_description.strip():
            st.error("Please provide a Job Description!")
        else:
            with st.spinner("Analyzing resumes... Please wait..."):
                results = process_resumes(resume_folder, job_description)
                st.session_state['results'] = results
                st.session_state['processed'] = True

# Results Display
if 'processed' in st.session_state:
    results = st.session_state['results']
    
    # Recalculate decision based on UI threshold
    results['Decision'] = results['Score'].apply(lambda x: "Shortlisted" if x >= threshold else "Rejected")
    
    # Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    total_resumes = len(results)
    shortlisted_count = len(results[results['Decision'] == "Shortlisted"])
    avg_score = results['Score'].mean()
    
    m1.metric("Total Resumes", total_resumes)
    m2.metric("Shortlisted", shortlisted_count, delta=f"{shortlisted_count/total_resumes:.1%}", delta_color="normal")
    m3.metric("Average Match", f"{avg_score:.1f}%")
    m4.metric("Top Score", f"{results['Score'].max():.1f}%")

    st.markdown("---")

    # Visualizations Row
    v1, v2 = st.columns(2)

    with v1:
        st.subheader("📊 Score Distribution")
        fig_hist = px.histogram(
            results, 
            x="Score", 
            nbins=20, 
            color="Decision",
            color_discrete_map={"Shortlisted": "#28a745", "Rejected": "#dc3545"},
            labels={"Score": "Match Score (%)"}
        )
        st.plotly_chart(fig_hist, use_container_width=True)

    with v2:
        st.subheader("📁 Category Breakdown")
        cat_counts = results.groupby(['Actual Category', 'Decision']).size().reset_index(name='Count')
        fig_bar = px.bar(
            cat_counts, 
            x="Actual Category", 
            y="Count", 
            color="Decision",
            barmode="group",
            color_discrete_map={"Shortlisted": "#28a745", "Rejected": "#dc3545"}
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")

    # Detailed Results Table
    st.subheader("📋 Screening Results")
    
    # Color-coded decision column
    def color_decision(val):
        color = '#d1e7dd' if val == 'Shortlisted' else '#f8d7da'
        return f'background-color: {color}'

    # Use .map() instead of .applymap() for newer pandas versions
    try:
        styled_results = results.style.map(color_decision, subset=['Decision'])
    except AttributeError:
        styled_results = results.style.applymap(color_decision, subset=['Decision'])
        
    st.dataframe(styled_results, use_container_width=True)

    # Download Options
    st.markdown("### 📥 Export")
    csv = results.to_csv(index=False)
    st.download_button(
        label="Download Full CSV Report",
        data=csv,
        file_name="screening_report.csv",
        mime="text/csv",
        use_container_width=True
    )

    # LinkedIn Shareable Section
    st.markdown("---")
    st.subheader("✨ LinkedIn Shareable Summary")
    
    top_candidates = results[results['Decision'] == "Shortlisted"].head(3)
    
    summary_box = f"""
    🚀 **Recruitment Update: AI Screening Complete!**
    
    We just finished screening **{total_resumes} resumes** for our new opening. 
    Using our AI-powered tool, we've identified **{shortlisted_count} top-tier candidates** 
    with a strong skill match.
    
    **Top Matching Skills Found:**
    {", ".join(results['Skills'].str.split(', ').explode().unique()[:8])}
    
    #Recruitment #AI #Hiring #DataScience #TechHiring
    """
    st.code(summary_box, language="markdown")
    st.info("💡 Copy the summary above to share your screening progress on LinkedIn!")

else:
    st.image("https://img.freepik.com/free-vector/human-resources-management-concept-hr-recruitment-hiring-job-application-concept-flat-vector-illustration_1200-435.jpg?w=1000", use_container_width=True)
    st.info("Enter a Job Description and click 'Screen Resumes' to get started!")
