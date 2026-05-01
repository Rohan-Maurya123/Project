import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
import plotly.express as px
import plotly.graph_objects as go

# Add the project root to sys.path so 'src' can be found when running streamlit directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import from local modules
from src.preprocess import clean_text, normalize_real_dataset
from src.predict import (
    load_model, predict_sentiment, detect_category, 
    get_priority, get_action, analyze_dataframe, 
    brand_health, top_keywords, create_sample_data
)
from src.train import train_sentiment_model

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Social Media Sentiment Analysis(Intelligence)",
    page_icon="📊",
    layout="wide"
)

# Apply CSS
css_path = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =====================================================
# MODEL LOADING / TRAINING
# =====================================================
@st.cache_resource
def get_model():
    model = load_model()
    if model is None:
        # If no model exists, train a quick one with sample data or dataset
        data_path = 'data/training.1600000.processed.noemoticon.csv'
        model, results_df, cm, labels, best_name = train_sentiment_model(data_path if os.path.exists(data_path) else None)
        return model, results_df, cm, labels, best_name
    
    # If model exists but we need results_df and cm for the info page, we'd need to re-evaluate
    # For now, let's just return the model and some placeholders if needed
    return model, None, None, ["Positive", "Negative", "Neutral"], "Loaded from Disk"

model, model_results_df, confusion_matrix_values, confusion_labels, best_model_name = get_model()

# =====================================================
# COLOR PALETTES
# =====================================================
sentiment_colors = {
    "Positive": "#22C55E",
    "Negative": "#EF4444",
    "Neutral": "#3B82F6"
}

multi_colors = [
    "#22C55E", "#EF4444", "#3B82F6", "#F59E0B", "#A855F7",
    "#06B6D4", "#EC4899", "#84CC16", "#F97316", "#14B8A6"
]

# =====================================================
# HEADER
# =====================================================
st.markdown("""
<div class="hero">
    <h1>📊 Social Media Sentiment Intelligence Dashboard</h1>
    <p>Advanced ML-powered social listening website for comments, reviews, complaints, campaigns, customer emotions, and brand reputation analytics.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="quote-box">
💬 “Behind every comment is a customer emotion. This dashboard converts public opinion into business intelligence.”
</div>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.title("🚀 Sentiment Intelligence")
st.sidebar.markdown("Analyze comments, detect sentiment, monitor complaints, and generate business insights.")

page = st.sidebar.radio(
    "Choose Section",
    [
        "🏠 Executive Home",
        "✍️ Single Comment Analyzer",
        "📂 Bulk CSV Analyzer",
        "📈 Premium Dashboard",
        "🔍 Keyword Intelligence",
        "🚨 Complaint Monitor",
        "📊 Campaign Analytics",
        "📤 Download Report"
    ]
)

st.sidebar.markdown("---")

if st.sidebar.button("🧪 Load Professional Sample Data"):
    sample_df = create_sample_data()
    st.session_state["data"] = analyze_dataframe(sample_df, model)
    st.sidebar.success("Sample data loaded successfully!")

# =====================================================
# EXECUTIVE HOME
# =====================================================
if page == "🏠 Executive Home":
    st.markdown('<div class="section-title">🏠 Executive Project Overview</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="glass-card">
            <h3>💬 Social Listening</h3>
            <p>Analyze customer comments, social media reviews, tweets, and feedback at scale.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="glass-card">
            <h3>🧠 ML Sentiment Engine</h3>
            <p>Uses TF-IDF and Logistic Regression to classify text as Positive, Negative, or Neutral.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="glass-card">
            <h3>📊 Business Intelligence</h3>
            <p>Generates brand health, complaint priority, keyword trends, and campaign insights.</p>
        </div>
        """, unsafe_allow_html=True)

    features = pd.DataFrame({
        "Premium Feature": [
            "ML Sentiment Classification",
            "Confidence Score",
            "Brand Health Score",
            "Complaint Category Detection",
            "Priority Tagging",
            "Platform Comparison",
            "Campaign Analytics",
            "Keyword Intelligence",
            "Business Action Recommendation",
            "Downloadable Report"
        ],
        "Recruiter Value": [
            "Shows NLP + ML knowledge",
            "Shows model interpretation",
            "Shows business KPI thinking",
            "Shows customer analytics logic",
            "Shows decision-making automation",
            "Shows dashboard analytics",
            "Shows marketing analytics use case",
            "Shows text mining ability",
            "Shows business intelligence skill",
            "Shows end-to-end project completion"
        ]
    })

    st.markdown("### ⭐ What Makes This Project Recruiter-Friendly?")
    st.dataframe(features, use_container_width=True)

# =====================================================
# SINGLE COMMENT ANALYZER
# =====================================================
elif page == "✍️ Single Comment Analyzer":
    st.markdown('<div class="section-title">✍️ Single Comment Sentiment Analyzer</div>', unsafe_allow_html=True)

    text = st.text_area(
        "Enter a customer comment, tweet, review, or feedback:",
        height=160,
        placeholder="Example: The app is amazing, but the delivery was very late."
    )

    if st.button("🚀 Analyze Sentiment"):
        if text.strip() == "":
            st.warning("Please enter a comment.")
        else:
            sentiment, confidence, cleaned = predict_sentiment(text, model)
            category = detect_category(text)
            priority = get_priority(sentiment, confidence)
            action = get_action(sentiment, category)

            card_color = "green" if sentiment == "Positive" else "red" if sentiment == "Negative" else "blue"

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.markdown(f"""
                <div class="metric-card {card_color}">
                    <div class="metric-value">{sentiment}</div>
                    <div class="metric-label">Predicted Sentiment</div>
                </div>
                """, unsafe_allow_html=True)

            with c2:
                st.markdown(f"""
                <div class="metric-card purple">
                    <div class="metric-value">{confidence}%</div>
                    <div class="metric-label">ML Confidence</div>
                </div>
                """, unsafe_allow_html=True)

            with c3:
                st.markdown(f"""
                <div class="metric-card yellow">
                    <div class="metric-value">{priority}</div>
                    <div class="metric-label">Priority Level</div>
                </div>
                """, unsafe_allow_html=True)

            with c4:
                st.markdown(f"""
                <div class="metric-card cyan">
                    <div class="metric-value">TF-IDF</div>
                    <div class="metric-label">Feature Method</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("### 🧹 Cleaned Text")
            st.code(cleaned)

            st.markdown("### 🏷️ Business Category")
            st.success(category)

            st.markdown("### 💡 Recommended Business Action")
            st.info(action)

# =====================================================
# BULK CSV ANALYZER
# =====================================================
elif page == "📂 Bulk CSV Analyzer":
    st.markdown('<div class="section-title">📂 Bulk CSV / Real Dataset Analyzer</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h3>📂 Upload Social Media Dataset</h3>
        <p>Upload tweets, YouTube comments, product reviews, customer feedback, or social media comments.</p>
        <p><b>Required:</b> Any one text column such as text, tweet, comment, comments, review, feedback, selected_text.</p>
        <p><b>Optional:</b> sentiment, platform, campaign, date columns.</p>
    </div>
    """, unsafe_allow_html=True)

    file = st.file_uploader("Upload CSV File", type=["csv"])

    if file:
        raw_df = pd.read_csv(file)

        st.markdown("### 📌 Original Dataset Preview")
        st.dataframe(raw_df.head(10), use_container_width=True)

        normalized_df, error = normalize_real_dataset(raw_df)

        if error:
            st.error(error)
            st.write("Available columns:", list(raw_df.columns))
        else:
            analyzed = analyze_dataframe(normalized_df, model)

            if "Real_Sentiment" in normalized_df.columns:
                analyzed["Real_Sentiment"] = normalized_df["Real_Sentiment"].values

                matched = (analyzed["Sentiment"] == analyzed["Real_Sentiment"]).sum()
                total_labeled = analyzed["Real_Sentiment"].notna().sum()
                real_match_score = round((matched / total_labeled) * 100, 2) if total_labeled > 0 else 0

                st.markdown(f"""
                <div class="metric-card green">
                    <div class="metric-value">{real_match_score}%</div>
                    <div class="metric-label">Prediction Match With Real Labels</div>
                </div>
                """, unsafe_allow_html=True)

            st.session_state["data"] = analyzed

            st.success("✅ Real dataset sentiment analysis completed successfully!")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.markdown(f"""
                <div class="metric-card blue">
                    <div class="metric-value">{analyzed.shape[0]}</div>
                    <div class="metric-label">Total Rows</div>
                </div>
                """, unsafe_allow_html=True)

            with c2:
                st.markdown(f"""
                <div class="metric-card purple">
                    <div class="metric-value">{analyzed.shape[1]}</div>
                    <div class="metric-label">Total Columns</div>
                </div>
                """, unsafe_allow_html=True)

            with c3:
                st.markdown(f"""
                <div class="metric-card yellow">
                    <div class="metric-value">CSV</div>
                    <div class="metric-label">Dataset Type</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("### ✅ Final Analyzed Dataset")
            st.dataframe(analyzed.head(30), use_container_width=True)

            st.markdown("### 🥧 Uploaded Dataset Sentiment Distribution")
            fig_uploaded = px.pie(
                analyzed,
                names="Sentiment",
                hole=0.45,
                color="Sentiment",
                color_discrete_map=sentiment_colors
            )
            fig_uploaded.update_traces(textposition="inside", textinfo="percent+label")
            fig_uploaded.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_uploaded, use_container_width=True)

            st.markdown("### 🌈 Uploaded Dataset Category Distribution")
            category_df = analyzed["Category"].value_counts().reset_index()
            category_df.columns = ["Category", "Count"]

            fig_cat = px.bar(
                category_df,
                x="Category",
                y="Count",
                color="Category",
                text="Count",
                color_discrete_sequence=multi_colors
            )
            fig_cat.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_cat, use_container_width=True)

            csv = analyzed.to_csv(index=False).encode("utf-8")
            st.download_button(
                "⬇️ Download Analyzed CSV",
                csv,
                "sentiment_analysis_results.csv",
                "text/csv"
            )

# =====================================================
# PREMIUM DASHBOARD
# =====================================================
elif page == "📈 Premium Dashboard":
    st.markdown('<div class="section-title">📈 Premium Sentiment Dashboard</div>', unsafe_allow_html=True)

    if "data" not in st.session_state:
        st.warning("Please load sample data or upload CSV first.")
    else:
        df = st.session_state["data"].copy()

        st.markdown("### 🎛️ Smart Filters")
        f1, f2, f3 = st.columns(3)

        with f1:
            selected_sentiment = st.multiselect(
                "Filter by Sentiment",
                options=df["Sentiment"].unique(),
                default=list(df["Sentiment"].unique())
            )

        with f2:
            selected_platform = st.multiselect(
                "Filter by Platform",
                options=df["platform"].unique(),
                default=list(df["platform"].unique())
            )

        with f3:
            selected_category = st.multiselect(
                "Filter by Category",
                options=df["Category"].unique(),
                default=list(df["Category"].unique())
            )

        df = df[
            (df["Sentiment"].isin(selected_sentiment)) &
            (df["platform"].isin(selected_platform)) &
            (df["Category"].isin(selected_category))
        ]

        total = len(df)
        positive = (df["Sentiment"] == "Positive").sum()
        negative = (df["Sentiment"] == "Negative").sum()
        neutral = (df["Sentiment"] == "Neutral").sum()
        health = brand_health(df)
        avg_conf = round(df["Confidence"].mean(), 2) if total > 0 else 0

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:
            st.markdown(f'<div class="metric-card blue"><div class="metric-value">{total}</div><div class="metric-label">Total Comments</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="metric-card green"><div class="metric-value">{positive}</div><div class="metric-label">Positive</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="metric-card red"><div class="metric-value">{negative}</div><div class="metric-label">Negative</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown(f'<div class="metric-card purple"><div class="metric-value">{neutral}</div><div class="metric-label">Neutral</div></div>', unsafe_allow_html=True)
        with c5:
            st.markdown(f'<div class="metric-card yellow"><div class="metric-value">{health}%</div><div class="metric-label">Brand Health</div></div>', unsafe_allow_html=True)

        st.markdown("### 🥧 Sentiment Distribution")
        fig1 = px.pie(
            df,
            names="Sentiment",
            hole=0.48,
            color="Sentiment",
            color_discrete_map=sentiment_colors
        )
        fig1.update_traces(textposition="inside", textinfo="percent+label")
        fig1.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown("### 🌈 Colorful Category Distribution")
        category_count = df["Category"].value_counts().reset_index()
        category_count.columns = ["Category", "Count"]

        fig2 = px.bar(
            category_count,
            x="Category",
            y="Count",
            color="Category",
            color_discrete_sequence=multi_colors,
            text="Count"
        )
        fig2.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("### 📊 Sentiment by Category")
        fig3 = px.histogram(
            df,
            x="Category",
            color="Sentiment",
            barmode="group",
            color_discrete_map=sentiment_colors
        )
        fig3.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown("### 📈 Sentiment Trend Over Time")
        df["date"] = pd.to_datetime(df["date"])
        trend = df.groupby(["date", "Sentiment"]).size().reset_index(name="Count")

        fig4 = px.line(
            trend,
            x="date",
            y="Count",
            color="Sentiment",
            markers=True,
            color_discrete_map=sentiment_colors
        )
        fig4.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig4, use_container_width=True)

        st.markdown("### 💡 Auto Business Insights")

        if health >= 40:
            st.markdown('<div class="insight">✅ Brand reputation is strong. Positive sentiment is clearly dominating.</div>', unsafe_allow_html=True)
        elif health >= 10:
            st.markdown('<div class="insight">⚠️ Brand sentiment is stable but should be monitored regularly.</div>', unsafe_allow_html=True)
        elif health >= 0:
            st.markdown('<div class="insight">⚠️ Brand sentiment is slightly positive, but negative feedback is meaningful.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="insight">🚨 Brand health is weak. Negative feedback needs urgent attention.</div>', unsafe_allow_html=True)

        if total > 0:
            top_category = df["Category"].value_counts().idxmax()
            st.markdown(f'<div class="insight">📍 Most discussed category: <b>{top_category}</b></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="insight">🧠 Average ML confidence score: <b>{avg_conf}%</b></div>', unsafe_allow_html=True)

# =====================================================
# KEYWORD INTELLIGENCE
# =====================================================
elif page == "🔍 Keyword Intelligence":
    st.markdown('<div class="section-title">🔍 Keyword Intelligence</div>', unsafe_allow_html=True)

    if "data" not in st.session_state:
        st.warning("Please load sample data or upload CSV first.")
    else:
        df = st.session_state["data"]

        keyword_df = top_keywords(df, 15)

        fig = px.bar(
            keyword_df,
            x="Keyword",
            y="Frequency",
            color="Keyword",
            color_discrete_sequence=multi_colors,
            text="Frequency",
            title="Most Repeated Customer Keywords"
        )
        fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)

        st.dataframe(keyword_df, use_container_width=True)

# =====================================================
# COMPLAINT MONITOR
# =====================================================
elif page == "🚨 Complaint Monitor":
    st.markdown('<div class="section-title">🚨 Complaint Monitor</div>', unsafe_allow_html=True)

    if "data" not in st.session_state:
        st.warning("Please load sample data or upload CSV first.")
    else:
        df = st.session_state["data"]

        complaints = df[df["Sentiment"] == "Negative"]

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(f'<div class="metric-card red"><div class="metric-value">{len(complaints)}</div><div class="metric-label">Total Complaints</div></div>', unsafe_allow_html=True)

        with c2:
            high_priority = (complaints["Priority"] == "High").sum()
            st.markdown(f'<div class="metric-card yellow"><div class="metric-value">{high_priority}</div><div class="metric-label">High Priority</div></div>', unsafe_allow_html=True)

        with c3:
            unique_categories = complaints["Category"].nunique()
            st.markdown(f'<div class="metric-card purple"><div class="metric-value">{unique_categories}</div><div class="metric-label">Issue Types</div></div>', unsafe_allow_html=True)

        if len(complaints) == 0:
            st.success("No negative complaints found.")
        else:
            st.markdown("### 📌 Complaint Table")
            st.dataframe(complaints, use_container_width=True)

            fig = px.histogram(
                complaints,
                x="Category",
                color="Priority",
                color_discrete_sequence=multi_colors,
                title="Complaint Categories by Priority"
            )
            fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)

# =====================================================
# CAMPAIGN ANALYTICS
# =====================================================
elif page == "📊 Campaign Analytics":
    st.markdown('<div class="section-title">📊 Campaign & Platform Analytics</div>', unsafe_allow_html=True)

    if "data" not in st.session_state:
        st.warning("Please load sample data or upload CSV first.")
    else:
        df = st.session_state["data"]

        st.markdown("### 📱 Platform-wise Sentiment")
        fig1 = px.histogram(
            df,
            x="platform",
            color="Sentiment",
            barmode="group",
            color_discrete_map=sentiment_colors
        )
        fig1.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown("### 🎯 Campaign-wise Sentiment")
        fig2 = px.histogram(
            df,
            x="campaign",
            color="Sentiment",
            barmode="group",
            color_discrete_map=sentiment_colors
        )
        fig2.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("### 🧩 Sentiment Share by Campaign")
        fig3 = px.sunburst(
            df,
            path=["campaign", "Sentiment"],
            color="Sentiment",
            color_discrete_map=sentiment_colors
        )
        fig3.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig3, use_container_width=True)

# =====================================================
# DOWNLOAD REPORT
# =====================================================
elif page == "📤 Download Report":
    st.markdown('<div class="section-title">📤 Download Analysis Report</div>', unsafe_allow_html=True)
    
    if "data" not in st.session_state:
        st.warning("Please load sample data or upload CSV first.")
    else:
        df = st.session_state["data"]
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download Full Analysis Report (CSV)",
            csv,
            "sentiment_report.csv",
            "text/csv"
        )
        st.success("Report is ready for download!")
