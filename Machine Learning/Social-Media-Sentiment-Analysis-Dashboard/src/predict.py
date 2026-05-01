import pandas as pd
import numpy as np
import joblib
import os
from collections import Counter
from src.preprocess import clean_text, add_missing_columns

def load_model():
    """
    Loads the trained model from the models directory.
    """
    model_path = 'models/sentiment_model.pkl'
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

def predict_sentiment(text, model):
    """
    Predicts the sentiment of a given text using the provided model.
    """
    if model is None:
        return "Unknown", 0.0, clean_text(text)
    
    cleaned = clean_text(text)
    prediction = model.predict([cleaned])[0]
    probabilities = model.predict_proba([cleaned])[0]
    confidence = round(np.max(probabilities) * 100, 2)
    return prediction, confidence, cleaned

def detect_category(text):
    """
    Detects the business category based on keywords in the text.
    """
    text = clean_text(text)

    categories = {
        "Delivery Issue": ["delivery", "late", "delay", "order", "rider", "shipping"],
        "Payment Issue": ["payment", "refund", "money", "transaction", "upi", "deducted"],
        "App Issue": ["app", "crash", "bug", "login", "loading", "screen", "update"],
        "Customer Support": ["support", "reply", "help", "customer", "agent", "complaint"],
        "Pricing Issue": ["price", "cost", "expensive", "charge", "fee"],
        "Product Quality": ["quality", "food", "product", "damaged", "taste", "packaging"],
        "Campaign Feedback": ["offer", "discount", "campaign", "ad", "promotion", "sale"]
    }

    matched = []
    for category, words in categories.items():
        if any(word in text for word in words):
            matched.append(category)

    return matched[0] if matched else "General Feedback"

def get_priority(sentiment, confidence):
    """
    Assigns a priority level based on sentiment and confidence.
    """
    if sentiment == "Negative" and confidence >= 65:
        return "High"
    elif sentiment == "Negative":
        return "Medium"
    elif sentiment == "Neutral":
        return "Low"
    return "Positive"

def get_action(sentiment, category):
    """
    Provides a recommended business action based on sentiment and category.
    """
    if sentiment == "Negative":
        return f"Review urgently. Main issue detected: {category}."
    elif sentiment == "Positive":
        return "Use this feedback as testimonial or campaign proof."
    return "Monitor this feedback for future trend analysis."

def analyze_dataframe(df, model):
    """
    Performs batch analysis on a dataframe of text.
    """
    df = add_missing_columns(df.copy())

    results = df["text"].apply(lambda x: predict_sentiment(x, model))

    df["Sentiment"] = results.apply(lambda x: x[0])
    df["Confidence"] = results.apply(lambda x: x[1])
    df["Cleaned_Text"] = results.apply(lambda x: x[2])
    df["Category"] = df["text"].apply(detect_category)
    df["Priority"] = df.apply(lambda row: get_priority(row["Sentiment"], row["Confidence"]), axis=1)
    df["Recommended_Action"] = df.apply(lambda row: get_action(row["Sentiment"], row["Category"]), axis=1)

    return df

def brand_health(df):
    """
    Calculates the brand health score.
    """
    total = len(df)
    if total == 0:
        return 0
    positive = (df["Sentiment"] == "Positive").sum()
    negative = (df["Sentiment"] == "Negative").sum()
    return round(((positive - negative) / total) * 100, 2)

def top_keywords(df, n=15):
    """
    Extracts the most frequent keywords from the cleaned text.
    """
    words = " ".join(df["Cleaned_Text"].astype(str)).split()
    words = [word for word in words if len(word) > 3]
    return pd.DataFrame(Counter(words).most_common(n), columns=["Keyword", "Frequency"])

def create_sample_data():
    """
    Creates a sample dataframe for testing/demonstration.
    """
    comments = [
        "I love this app, it is smooth and fast",
        "Worst delivery experience ever, my order was late",
        "The product quality is okay, nothing special",
        "Payment failed but money was deducted",
        "Customer support was very helpful and polite",
        "The app keeps crashing after login",
        "Amazing discount campaign, loved the offer",
        "Food quality was poor and delivery was delayed",
        "The service is average",
        "Great product and very fast delivery",
        "Refund process is too slow and frustrating",
        "The new update is excellent",
        "Price is too expensive compared to competitors",
        "Support team did not reply to my complaint",
        "I am happy with the overall experience",
        "The app UI is beautiful and easy to use",
        "Bad packaging and damaged product received",
        "Offer was good but delivery was late",
        "Normal service, nothing very good or bad",
        "I will recommend this platform to my friends",
        "The login screen has a bug",
        "The festive offer was amazing",
        "Product packaging was damaged",
        "The customer agent helped me quickly",
        "The app update is acceptable"
    ]

    return pd.DataFrame({"text": comments})
