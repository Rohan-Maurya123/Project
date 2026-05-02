import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib
import sys
import os
import requests
import time
import random
from streamlit_lottie import st_lottie
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Add root directory to path to import src modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model_trainer import SentimentModel
from src.preprocessing import TextPreprocessor

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="✨",
    layout="wide"
)

# Custom CSS for Premium Look
def inject_custom_css():
    st.markdown("""
    <style>
    /* Glassmorphism effect */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }
    
    /* Enhance Text Visibility */
    p, span, label, .stMarkdown {
        color: #ffffff !important;
        font-weight: 500 !important;
        text-shadow: 0px 1px 2px rgba(0,0,0,0.5);
    }

    .main {
        background: transparent;
    }

    /* Card styling */
    div[data-testid="stVerticalBlock"] > div:has(div.stMetric) {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease;
    }
    
    div[data-testid="stVerticalBlock"] > div:has(div.stMetric):hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.08);
    }

    /* Smooth Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stMarkdown, .stButton, .stMetric, .stPlotlyChart {
        animation: fadeIn 0.8s ease-out forwards;
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        border: none;
        padding: 10px 25px;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(37, 117, 252, 0.4);
        color: white;
    }

    /* Sidebar glassmorphism */
    [data-testid="stSidebar"] {
        background-color: rgba(20, 20, 30, 0.8) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Custom Title Color */
    h1 {
        background: linear-gradient(to right, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Load model and preprocessor
@st.cache_resource
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

@st.cache_resource
def load_sentiment_model():
    model = SentimentModel()
    try:
        model.load_model('models/sentiment_model.joblib', 'models/tfidf_vectorizer.joblib')
    except:
        st.error("Model files not found! Please run 'python main.py' first to train the model.")
        return None
    return model

# Main UI
def main():
    inject_custom_css()
    
    # Sidebar Navigation
    st.sidebar.title("🚀 Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Analytics Dashboard", "Sentiment Explorer", "Real-time Simulation"])
    
    model = load_sentiment_model()
    
    if page == "Home":
        show_home_page()
    elif page == "Analytics Dashboard":
        show_analytics_page(model)
    elif page == "Sentiment Explorer":
        show_explorer_page(model)
    elif page == "Real-time Simulation":
        show_simulation_page(model)

def show_home_page():
    col_title, col_lottie = st.columns([2, 1])
    with col_title:
        st.title("✨Sentiment Analysis")
        st.markdown("""
        <div style='background: rgba(255,255,255,0.1); padding: 25px; border-radius: 15px; border-left: 5px solid #00c6ff;'>
            <h3 style='color: white; margin-top:0;'>Welcome to the Future of NLP</h3>
            <p style='font-size: 1.1em;'>Our advanced Sentiment Analysis engine helps brands understand customer emotions at scale. 
            Navigate through the sidebar to explore detailed analytics, search through historical data, or witness real-time simulation.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_lottie:
        lottie_ai = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_M9pWAD.json")
        if lottie_ai:
            st_lottie(lottie_ai, height=200, key="home_anim")

    st.write("---")
    st.header("🛠️ Core Capabilities")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("📊 Deep Analytics")
        st.write("Visual distribution of sentiments with interactive charts.")
    with c2:
        st.subheader("🔍 Smart Search")
        st.write("Filter and explore specific keywords and their sentiment impact.")
    with c3:
        st.subheader("⚡ Real-time Feed")
        st.write("Simulate a live stream of social media data processing.")

def show_analytics_page(model):
    st.header("📊 Sentiment Analytics Dashboard")
    
    analysis_mode = st.radio("Choose Mode", ["Single Text Analysis", "Bulk Analysis (CSV)"], horizontal=True)
    
    if analysis_mode == "Single Text Analysis":
        user_input = st.text_area("Enter a social media post/comment:", "I am so happy with this project!", height=100)
        
        if st.button("Analyze Sentiment"):
            if model:
                prediction = model.predict(user_input)
                sentiment = "Positive" if prediction[0] == 1 else "Negative"
                
                if sentiment == "Positive":
                    st.markdown(f"""
                    <div style='background: rgba(0, 255, 136, 0.15); padding: 30px; border-radius: 20px; border: 2px solid #00ff88; text-align: center;'>
                        <h1 style='color: #00ff88; margin: 0;'>😊 Positive Sentiment</h1>
                        <p style='color: white; font-size: 1.2em;'>Optimistic and favorable tone detected.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style='background: rgba(255, 75, 75, 0.15); padding: 30px; border-radius: 20px; border: 2px solid #ff4b4b; text-align: center;'>
                        <h1 style='color: #ff4b4b; margin: 0;'>😠 Negative Sentiment</h1>
                        <p style='color: white; font-size: 1.2em;'>Critical or unfavorable tone detected.</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.error("Model not loaded.")

    else:
        uploaded_file = st.file_uploader("Upload your CSV file (must have a 'text' column)", type=['csv'])
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            if 'text' in df.columns:
                if st.button("Generate Detailed Report"):
                    with st.spinner("Processing deep analytics..."):
                        df['prediction'] = model.predict(df['text'].tolist())
                        df['sentiment'] = df['prediction'].apply(lambda x: "Positive" if x == 1 else "Negative")
                        df['text_length'] = df['text'].apply(len)
                    
                    # Metrics Row
                    st.subheader("📈 Key Metrics")
                    m1, m2, m3, m4 = st.columns(4)
                    total = len(df)
                    pos = len(df[df['sentiment'] == 'Positive'])
                    neg = len(df[df['sentiment'] == 'Negative'])
                    avg_len = df['text_length'].mean()
                    
                    m1.metric("Total Data", total)
                    m2.metric("Positive", f"{(pos/total)*100:.1f}%")
                    m3.metric("Negative", f"{(neg/total)*100:.1f}%")
                    m4.metric("Avg Length", f"{avg_len:.0f} chars")
                    
                    # Visualizations Row 1
                    col1, col2 = st.columns(2)
                    with col1:
                        fig_pie = px.pie(df, names='sentiment', title='Sentiment Distribution',
                                       color='sentiment', color_discrete_map={'Positive':'#00ff88', 'Negative':'#ff4b4b'},
                                       hole=0.4)
                        fig_pie.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)')
                        st.plotly_chart(fig_pie, use_container_width=True)
                    
                    with col2:
                        fig_len = px.histogram(df, x="text_length", color="sentiment", 
                                             title="Text Length Distribution",
                                             color_discrete_map={'Positive':'#00ff88', 'Negative':'#ff4b4b'},
                                             marginal="box")
                        fig_len.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)')
                        st.plotly_chart(fig_len, use_container_width=True)

                    # Visualizations Row 2 (Word Cloud)
                    st.subheader("☁️ Word Cloud Analysis")
                    wc_col1, wc_col2 = st.columns(2)
                    
                    with wc_col1:
                        st.write("Positive Keywords")
                        pos_text = " ".join(df[df['sentiment']=='Positive']['text'])
                        if pos_text:
                            wc_pos = WordCloud(background_color="black", colormap='Greens', width=400, height=200).generate(pos_text)
                            st.image(wc_pos.to_array())
                    
                    with wc_col2:
                        st.write("Negative Keywords")
                        neg_text = " ".join(df[df['sentiment']=='Negative']['text'])
                        if neg_text:
                            wc_neg = WordCloud(background_color="black", colormap='Reds', width=400, height=200).generate(neg_text)
                            st.image(wc_neg.to_array())

                    st.subheader("📋 Raw Data Sample")
                    st.dataframe(df[['text', 'sentiment', 'text_length']].head(50))

def show_explorer_page(model):
    st.header("🔍 Sentiment Explorer")
    st.write("Filter and explore datasets based on keywords and sentiment.")
    
    uploaded_file = st.file_uploader("Upload CSV to Explore", type=['csv'], key="explorer_upload")
    if uploaded_file:
        # Read the first few lines to check for headers
        try:
            # Sentiment140 usually has no headers. We'll try to detect or ask the user.
            df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
            
            # If the dataset looks like Sentiment140 (6 columns, no headers)
            if len(df.columns) == 6 and df.columns[0] != 'target':
                st.info("Detecting Sentiment140 format (no headers). Adjusting...")
                df.columns = ['target', 'id', 'date', 'flag', 'user', 'text']
            
            # Let user select the text column if 'text' isn't found
            text_col = 'text'
            if text_col not in df.columns:
                text_col = st.selectbox("Select the column containing the text/tweets:", df.columns)
            
            if text_col:
                # Limit to 5000 rows for performance in explorer
                if len(df) > 5000:
                    st.warning("Dataset is large. Showing a sample of 5,000 rows for performance.")
                    df = df.sample(5000, random_state=42)

                search_query = st.text_input("Search keywords (e.g., 'bad', 'great', 'service')")
                
                # Predict or Normalize sentiments
                with st.spinner("Analyzing sentiments..."):
                    if 'sentiment' not in df.columns:
                        # Clean labels if it's the target column (0, 4)
                        if 'target' in df.columns:
                            df['sentiment'] = df['target'].apply(lambda x: "Positive" if x == 4 or x == 1 else "Negative")
                        else:
                            # Use model to predict
                            df['prediction'] = model.predict(df[text_col].astype(str).tolist())
                            df['sentiment'] = df['prediction'].apply(lambda x: "Positive" if x == 1 else "Negative")
                    else:
                        # Normalize existing sentiment column to Title Case (e.g., 'positive' -> 'Positive')
                        df['sentiment'] = df['sentiment'].astype(str).str.title()
                
                # Dynamic filter options based on data
                available_sentiments = df['sentiment'].unique().tolist()
                sentiment_filter = st.multiselect("Filter by Sentiment", available_sentiments, default=available_sentiments)
                
                # Apply Filters
                filtered_df = df[df['sentiment'].isin(sentiment_filter)]
                if search_query:
                    # Case-insensitive search
                    filtered_df = filtered_df[filtered_df[text_col].str.contains(search_query, case=False, na=False)]
                
                st.success(f"Showing {len(filtered_df)} results")
                
                # Display Results with highlighted sentiment
                st.dataframe(
                    filtered_df[[text_col, 'sentiment']].reset_index(drop=True),
                    use_container_width=True
                )
        except Exception as e:
            st.error(f"Error reading file: {e}")

def show_simulation_page(model):
    st.header("⚡ Real-time Simulation Feed")
    st.write("Simulating a live social media stream...")
    
    sample_posts = [
        "This is the best service ever! I am so happy.",
        "Terrible experience, the app keeps crashing.",
        "I love the new update, works perfectly.",
        "Waste of money, I want a refund.",
        "Absolutely amazing work by the team!",
        "Poor customer support, very disappointed.",
        "Great quality product, highly recommended.",
        "The delivery was late and the box was damaged."
    ]
    
    if st.button("Start Live Stream"):
        feed_container = st.empty()
        log_data = []
        
        for i in range(10):
            post = random.choice(sample_posts)
            pred = model.predict(post)[0]
            sentiment = "Positive" if pred == 1 else "Negative"
            color = "#00ff88" if sentiment == "Positive" else "#ff4b4b"
            
            log_data.insert(0, {"Time": time.strftime("%H:%M:%S"), "Post": post, "Sentiment": sentiment})
            
            with feed_container.container():
                st.markdown(f"""
                <div style='background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; border-left: 5px solid {color}; margin-bottom: 10px;'>
                    <small style='color: #aaa;'>{time.strftime("%H:%M:%S")}</small><br>
                    <b style='color: {color};'>{sentiment}</b>: {post}
                </div>
                """, unsafe_allow_html=True)
            
            time.sleep(1.5)
        
        st.success("Simulation Complete!")
        st.subheader("Simulation History")
        st.table(pd.DataFrame(log_data))

if __name__ == "__main__":
    main()
