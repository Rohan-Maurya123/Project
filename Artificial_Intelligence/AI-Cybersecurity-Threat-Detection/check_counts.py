import pandas as pd
print("Script started...")
from src.data_loader import load_data
from src.preprocess import preprocess_data
import joblib
import os

def check():
    # Load test data
    test_df = load_data("data/test.csv")
    print(f"Raw Test Shape: {test_df.shape}")

    # Preprocess
    test_df_processed = preprocess_data(test_df, training=False)
    
    # Load model
    if os.path.exists("models/model.pkl"):
        model = joblib.load("models/model.pkl")
        X_test = test_df_processed.drop('label', axis=1)
        predictions = model.predict(X_test)
        
        num_threats = sum(predictions)
        total = len(predictions)
        print(f"Predictions: {num_threats} threats out of {total}")
        
        if 'label' in test_df_processed.columns:
            y_test = test_df_processed['label']
            from sklearn.metrics import classification_report, confusion_matrix
            print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
            print("\nClassification Report:\n", classification_report(y_test, predictions))
    else:
        print("Model file not found!")

if __name__ == "__main__":
    check()
