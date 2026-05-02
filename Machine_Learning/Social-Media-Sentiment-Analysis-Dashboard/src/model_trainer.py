import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from src.preprocessing import TextPreprocessor
from src.data_loader import load_data

class SentimentModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000)
        self.model = LogisticRegression(max_iter=1000)
        self.preprocessor = TextPreprocessor()

    def train(self, df):
        """
        Trains the sentiment model using the provided dataframe.
        """
        print("Starting preprocessing...")
        # Preprocess the text
        df['processed_text'] = df['text'].apply(self.preprocessor.preprocess)
        
        # Split data
        X = df['processed_text']
        y = df['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print("Vectorizing text data...")
        # Vectorization
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)
        
        print("Training Logistic Regression model...")
        # Model training
        self.model.fit(X_train_vec, y_train)
        
        # Evaluation
        y_pred = self.model.predict(X_test_vec)
        print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
        
        return y_test, y_pred

    def save_model(self, model_path='models/sentiment_model.joblib', vectorizer_path='models/tfidf_vectorizer.joblib'):
        """
        Saves the trained model and vectorizer to files.
        """
        if not os.path.exists('models'):
            os.makedirs('models')
        joblib.dump(self.model, model_path)
        joblib.dump(self.vectorizer, vectorizer_path)
        print(f"Model saved to {model_path} and vectorizer saved to {vectorizer_path}")

    def load_model(self, model_path='models/sentiment_model.joblib', vectorizer_path='models/tfidf_vectorizer.joblib'):
        """
        Loads the model and vectorizer from files.
        """
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        print("Model and vectorizer loaded successfully.")

    def predict(self, text):
        """
        Predicts sentiment for a single text input or list of texts.
        """
        if isinstance(text, str):
            text = [text]
        
        processed_texts = [self.preprocessor.preprocess(t) for t in text]
        vec_text = self.vectorizer.transform(processed_texts)
        prediction = self.model.predict(vec_text)
        
        return prediction

if __name__ == "__main__":
    # Example usage
    data_path = 'data/training.1600000.processed.noemoticon.csv'
    df = load_data(data_path)
    
    # If using full dataset, we might want to sample it for faster training during development
    if len(df) > 10000:
        df = df.sample(10000, random_state=42)
    
    # Mapping Sentiment140 labels (0=Neg, 4=Pos) to (0=Neg, 1=Pos)
    if 4 in df['target'].unique():
        df['target'] = df['target'].replace(4, 1)
        
    trainer = SentimentModel()
    trainer.train(df)
    trainer.save_model()
