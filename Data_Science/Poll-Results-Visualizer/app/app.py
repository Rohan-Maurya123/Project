import streamlit as st
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import load_data
from src.preprocessing import clean_data
from src.analysis import (
    get_response_counts,
    get_percentage,
    region_analysis,
    age_analysis
)
from src.visualization import plot_interactive_bar, plot_stacked_bar
from src.insights import generate_insights

st.set_page_config(page_title="Poll Visualizer", layout="wide", page_icon="📊")

# Custom CSS for styling
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
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Poll Results Visualizer")
st.markdown("---")

# Sidebar Filters
st.sidebar.header("🔍 Filters")

# Load Data
df = load_data()
df = clean_data(df)

# Region Filter
all_regions = ["All"] + sorted(df["Region"].unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", all_regions)

# Age Group Filter
all_ages = ["All"] + sorted(df["Age_Group"].unique().tolist())
selected_age = st.sidebar.multiselect("Select Age Groups", all_ages, default="All")

# Apply Filters
filtered_df = df.copy()
if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

if "All" not in selected_age and len(selected_age) > 0:
    filtered_df = filtered_df[filtered_df["Age_Group"].isin(selected_age)]

# Analysis on filtered data
response_counts = get_response_counts(filtered_df)
percentage = get_percentage(filtered_df)
region_data = region_analysis(filtered_df)
age_data = age_analysis(filtered_df)

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Responses", len(filtered_df))
with col2:
    top_response = response_counts.idxmax() if not response_counts.empty else "N/A"
    st.metric("Top Preference", top_response)
with col3:
    top_region = filtered_df["Region"].mode()[0] if not filtered_df.empty else "N/A"
    st.metric("Most Active Region", top_region)
with col4:
    unique_days = filtered_df["Date"].nunique() if not filtered_df.empty else 0
    st.metric("Survey Duration (Days)", unique_days)

st.markdown("---")

# Main Dashboard Layout
tab1, tab2, tab3 = st.tabs(["📈 Overview", "🌍 Segment Analysis", "📋 Data View"])

with tab1:
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("Response Distribution")
        if not response_counts.empty:
            st.altair_chart(plot_interactive_bar(response_counts, "Response", "Count", "Response Distribution"), use_container_width=True)
        else:
            st.warning("No data for selected filters.")

    with col_right:
        st.subheader("Percentage Share")
        if not percentage.empty:
            # Use a more visually appealing display for percentages
            st.dataframe(percentage.rename("Percentage (%)").map(lambda x: f"{x:.1f}%"), use_container_width=True)
        else:
            st.warning("No data for selected filters.")

    st.subheader("💡 Key Insights")
    if not response_counts.empty:
        st.info(generate_insights(response_counts))
    else:
        st.info("Select filters to see insights.")

with tab2:
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("Region-wise Analysis")
        if not region_data.empty:
            st.altair_chart(plot_stacked_bar(region_data, "Region", "Responses by Region"), use_container_width=True)
        else:
            st.warning("No data for selected filters.")

    with col_b:
        st.subheader("Age Group Analysis")
        if not age_data.empty:
            st.altair_chart(plot_stacked_bar(age_data, "Age_Group", "Responses by Age Group"), use_container_width=True)
        else:
            st.warning("No data for selected filters.")

with tab3:
    st.subheader("� Raw Data Preview")
    st.dataframe(filtered_df, use_container_width=True)
    
    # Download button for filtered data
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data",
        data=csv,
        file_name='filtered_poll_data.csv',
        mime='text/csv',
    )