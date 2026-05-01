import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Retail Forecasting Dashboard", layout="wide")

st.title("📊 Retail Sales Forecasting & Inventory Optimization")

# Load data - check both root and app/ relative paths
paths = ["outputs/final_output.csv", "../outputs/final_output.csv"]
DATA_PATH = next((p for p in paths if os.path.exists(p)), None)

if DATA_PATH is None:
    st.error("⚠️ Please run main.py first to generate output data.")
    st.info("Run command: `python main.py` in the root directory.")
else:
    df = pd.read_csv(DATA_PATH)
    df['date'] = pd.to_datetime(df['date'])

    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    
    # Category Filter
    all_categories = ["All"] + sorted(df['category'].unique().tolist())
    category = st.sidebar.selectbox("Select Category", all_categories)
    
    if category != "All":
        df_filtered_cat = df[df['category'] == category]
    else:
        df_filtered_cat = df

    # Product Filter
    product_id = st.sidebar.selectbox("Select Product", sorted(df_filtered_cat['product_id'].unique()))

    filtered_df = df_filtered_cat[df_filtered_cat['product_id'] == product_id]

    # KPIs
    st.subheader("📌 Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    total_sales = int(filtered_df['sales'].sum())
    avg_forecast = round(filtered_df['forecast'].mean(), 2)
    avg_reorder = round(filtered_df['reorder_point'].mean(), 2)
    avg_safety = round(filtered_df['safety_stock'].mean(), 2)

    col1.metric("Total Sales", f"{total_sales:,}")
    col2.metric("Avg Forecast", f"{avg_forecast:,}")
    col3.metric("Avg Reorder Point", f"{avg_reorder:,}")
    col4.metric("Avg Safety Stock", f"{avg_safety:,}")

    # Sales vs Forecast Plotly
    st.subheader("📈 Sales vs Forecast")
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_df['date'], y=filtered_df['sales'], 
                             name='Actual Sales', line=dict(color='royalblue', width=2)))
    fig.add_trace(go.Scatter(x=filtered_df['date'], y=filtered_df['forecast'], 
                             name='Forecasted Sales', line=dict(color='firebrick', width=2, dash='dot')))
    
    fig.update_layout(title=f"Sales History vs Forecast for {product_id}",
                      xaxis_title="Date", yaxis_title="Units Sold",
                      template="plotly_white", height=500)
    st.plotly_chart(fig, use_container_width=True)

    # Inventory Analysis
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("📦 Inventory Optimization Table")
        st.dataframe(filtered_df[['date', 'sales', 'forecast', 'safety_stock', 'reorder_point']].tail(10))
    
    with col_b:
        st.subheader("📉 Safety Stock vs Sales Variance")
        # Show variance over time
        fig_var = px.area(filtered_df, x='date', y='safety_stock', title="Safety Stock Level Over Time")
        st.plotly_chart(fig_var, use_container_width=True)

    # Download option
    st.sidebar.markdown("---")
    st.sidebar.download_button(
        label="📥 Download Results",
        data=filtered_df.to_csv(index=False),
        file_name=f"forecast_{product_id}.csv",
        mime="text/csv"
    )
    