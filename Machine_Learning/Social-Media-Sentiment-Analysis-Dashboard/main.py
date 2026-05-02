from src.data_loader import load_data
from src.model_trainer import SentimentModel
import os

def main():
    # 1. Load Data
    data_path = 'data/training.1600000.processed.noemoticon.csv'
    df = load_data(data_path)
    
    # 2. Sample data if too large (for quick demo)
    if len(df) > 20000:
        print("Sampling 20,000 records for demonstration training...")
        df = df.sample(20000, random_state=42)
    
    # 3. Clean target labels (0=Neg, 4=Pos) -> (0, 1)
    if 4 in df['target'].unique():
        df['target'] = df['target'].replace(4, 1)
    
    # 4. Initialize and Train Model
    sentiment_model = SentimentModel()
    sentiment_model.train(df)
    
    # 5. Save the trained model
    sentiment_model.save_model()
    
    # 6. Test Prediction
    test_tweets = [
        "I love this project! It's so helpful.",
        "I'm feeling very sad about the news today.",
        "The movie was okay, nothing special but not bad either."
    ]
    
    predictions = sentiment_model.predict(test_tweets)
    for tweet, pred in zip(test_tweets, predictions):
        sentiment = "Positive" if pred == 1 else "Negative"
        print(f"Tweet: {tweet} | Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
