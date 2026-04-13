from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.model import train_model
import joblib
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

def main():
    print("--- Starting Pipeline ---")
    
    # 1. Load and preprocess training data
    print("\nLoading training data...")
    train_df = load_data("data/train.csv")
    train_df = preprocess_data(train_df, training=True)
    
    # 2. Train model
    print("\nTraining model...")
    model = train_model(train_df)
    
    # 3. Load and preprocess test data
    print("\nLoading test data...")
    test_df = load_data("data/test.csv")
    test_df_processed = preprocess_data(test_df, training=False)
    
    # 4. Predict on test data
    print("\nEvaluating on test.csv...")
    X_test = test_df_processed.drop('label', axis=1)
    y_test = test_df_processed['label']
    
    predictions = model.predict(X_test)
    
    num_threats = sum(predictions)
    total = len(predictions)
    print(f"\nTest Result: {num_threats} threats out of {total} ({num_threats/total*100:.2f}%)")
    
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
    print("\nClassification Report:\n", classification_report(y_test, predictions))

if __name__ == "__main__":
    main()
