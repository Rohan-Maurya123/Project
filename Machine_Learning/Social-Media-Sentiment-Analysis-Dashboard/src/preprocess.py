import pandas as pd
import re

def clean_text(text):
    """
    Cleans the input text by removing URLs, mentions, hashtags, and non-alphabetic characters.
    """
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def normalize_real_dataset(df):
    """
    Normalizes different CSV formats to a standard format with a 'text' column.
    """
    df = df.copy()

    possible_text_columns = [
        "text", "tweet", "Tweet", "comment", "comments", "Comment",
        "content", "review", "Review", "selected_text",
        "message", "feedback", "Feedback", "body", "post"
    ]

    possible_sentiment_columns = [
        "sentiment", "Sentiment", "label", "Label", "category",
        "airline_sentiment", "sentiments", "target", "class"
    ]

    text_col = None
    sentiment_col = None

    for col in possible_text_columns:
        if col in df.columns:
            text_col = col
            break

    for col in possible_sentiment_columns:
        if col in df.columns:
            sentiment_col = col
            break

    if text_col is None:
        return None, "No valid text/comment column found."

    df = df.rename(columns={text_col: "text"})

    if sentiment_col is not None:
        df = df.rename(columns={sentiment_col: "Real_Sentiment"})
        df["Real_Sentiment"] = df["Real_Sentiment"].astype(str).str.strip().str.lower()

        mapping = {
            "positive": "Positive",
            "pos": "Positive",
            "1": "Positive",
            "4": "Positive",

            "negative": "Negative",
            "neg": "Negative",
            "-1": "Negative",
            "0": "Negative",

            "neutral": "Neutral",
            "neu": "Neutral",
            "2": "Neutral",

            "irrelevant": "Neutral",
            "mixed": "Neutral"
        }

        df["Real_Sentiment"] = df["Real_Sentiment"].map(mapping).fillna(df["Real_Sentiment"])

    df = df.dropna(subset=["text"])
    df = df[df["text"].astype(str).str.strip() != ""]

    return df, None

def add_missing_columns(df):
    """
    Adds synthetic columns like platform, campaign, and date if they are missing.
    """
    if "platform" not in df.columns:
        platforms = ["Instagram", "YouTube", "Twitter/X", "LinkedIn", "Facebook"]
        df["platform"] = [platforms[i % len(platforms)] for i in range(len(df))]

    if "campaign" not in df.columns:
        campaigns = ["Launch Campaign", "Festive Offer", "App Update", "Brand Awareness"]
        df["campaign"] = [campaigns[i % len(campaigns)] for i in range(len(df))]

    if "date" not in df.columns:
        dates = pd.date_range(end=pd.Timestamp.today(), periods=len(df)).date
        df["date"] = dates

    return df
