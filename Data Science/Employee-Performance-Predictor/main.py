import sys
import os
from src.data_generator import generate_data
from src.preprocessing import preprocess_data
from src.model import train_model
from src.evaluate import evaluate_model
from sklearn.model_selection import train_test_split
import joblib

def main():
    # Create necessary directories
    for folder in ["data", "models", "outputs"]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    print("Phase 1 & 2: Data Creation...")
    data = generate_data(n=1000)
    print(f"Dataset created with {len(data)} records.")

    print("\nPhase 3 & 5: Preprocessing & Feature Engineering...")
    X, y, encoders = preprocess_data(data, is_training=True)
    print(f"Features: {list(X.columns)}")

    print("\nPhase 6: Model Building (Random Forest with Tuning)...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)

    print("\nPhase 7: Evaluation...")
    acc, cm, report, feat_imp = evaluate_model(model, X_test, y_test)
    print(f"Model Accuracy: {acc:.2f}")
    print("\nClassification Report:\n", report)

    print("\nPhase 8: Insights (Top 5 Features)...")
    print(feat_imp.head())

    # Save assets
    joblib.dump({"model": model, "encoders": encoders}, "models/model.pkl")
    print("\nModel and encoders saved to models/model.pkl")
    print("Project Phase completion successful!")

if __name__ == "__main__":
    main()
