import pandas as pd
import numpy as np
import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from src.preprocess import clean_text

def train_sentiment_model(data_path=None):
    """
    Trains multiple sentiment analysis models and returns the best one.
    If data_path is provided, it trains on the CSV dataset.
    """
    if data_path and os.path.exists(data_path):
        # Load Sentiment140 dataset (specific format)
        try:
            # Sentiment140: 0=target, 1=id, 2=date, 3=flag, 4=user, 5=text
            df = pd.read_csv(data_path, encoding='latin-1', header=None)
            df.columns = ['target', 'id', 'date', 'flag', 'user', 'text']
            
            # Subsample for speed if it's too large (1.6M rows)
            if len(df) > 50000:
                df = df.sample(50000, random_state=42)
            
            # Map targets: 0 -> Negative, 2 -> Neutral, 4 -> Positive
            target_map = {0: 'Negative', 2: 'Neutral', 4: 'Positive'}
            df['sentiment'] = df['target'].map(target_map)
            training_data = df[['text', 'sentiment']]
        except Exception as e:
            print(f"Error loading dataset: {e}. Falling back to sample data.")
            training_data = get_sample_training_data()
    else:
        training_data = get_sample_training_data()

    training_data["cleaned"] = training_data["text"].apply(clean_text)

    X_train, X_test, y_train, y_test = train_test_split(
        training_data["cleaned"],
        training_data["sentiment"],
        test_size=0.25,
        random_state=42,
        stratify=training_data["sentiment"]
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Naive Bayes": MultinomialNB(),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    results = []
    trained_models = {}

    for name, classifier in models.items():
        pipeline = Pipeline([
            ("tfidf", TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
            ("classifier", classifier)
        ])

        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)

        results.append({
            "Model": name,
            "Accuracy": round(accuracy_score(y_test, y_pred) * 100, 2),
            "F1 Score": round(f1_score(y_test, y_pred, average="weighted") * 100, 2)
        })

        trained_models[name] = pipeline

    results_df = pd.DataFrame(results)
    best_model_name = results_df.sort_values(
        by=["F1 Score", "Accuracy"],
        ascending=False
    ).iloc[0]["Model"]

    best_model = trained_models[best_model_name]
    
    # Save the best model
    os.makedirs('models', exist_ok=True)
    joblib.dump(best_model, 'models/sentiment_model.pkl')
    
    best_pred = best_model.predict(X_test)
    cm = confusion_matrix(
        y_test,
        best_pred,
        labels=["Positive", "Negative", "Neutral"]
    )

    return best_model, results_df, cm, ["Positive", "Negative", "Neutral"], best_model_name

def get_sample_training_data():
    return pd.DataFrame({
        "text": [
            "I love this app it is amazing and smooth",
            "The service was excellent and very fast",
            "Great product and very helpful support",
            "I am very happy with the experience",
            "This platform is awesome and easy to use",
            "The delivery was quick and perfect",
            "Customer support was polite and helpful",
            "The offer is great and I loved it",
            "Very satisfied with the product quality",
            "The app design is beautiful and simple",

            "Worst service ever I hate this app",
            "The delivery was very late and bad",
            "Payment failed and money was deducted",
            "Customer support did not reply",
            "The app keeps crashing again and again",
            "Very poor experience and terrible service",
            "The product was damaged and bad",
            "Refund process is slow and frustrating",
            "This is expensive and not worth it",
            "I am disappointed with the quality",

            "The service is okay",
            "It is an average experience",
            "Nothing special about this product",
            "The app is normal",
            "The delivery was neither fast nor slow",
            "I have no strong opinion",
            "The product is fine",
            "The update is acceptable",
            "It works as expected",
            "The experience is neutral"
        ],
        "sentiment": [
            "Positive","Positive","Positive","Positive","Positive",
            "Positive","Positive","Positive","Positive","Positive",
            "Negative","Negative","Negative","Negative","Negative",
            "Negative","Negative","Negative","Negative","Negative",
            "Neutral","Neutral","Neutral","Neutral","Neutral",
            "Neutral","Neutral","Neutral","Neutral","Neutral"
        ]
    })

if __name__ == "__main__":
    data_file = 'data/training.1600000.processed.noemoticon.csv'
    print("Training model...")
    train_sentiment_model(data_file)
    print("Model trained and saved to models/sentiment_model.pkl")
