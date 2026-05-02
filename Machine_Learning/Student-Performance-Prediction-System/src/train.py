import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from preprocess import load_data, preprocess_data, get_train_test_split

def train_model():
    # 1. Load and Preprocess
    print("Loading data...")
    data_path = os.path.join('data', 'student-mat.csv')
    df = load_data(data_path)
    
    print("Preprocessing data...")
    df_processed, mappings = preprocess_data(df)
    
    X_train, X_test, y_train, y_test, scaler = get_train_test_split(df_processed)
    
    # 2. Train Model
    print("Training Random Forest Model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 3. Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # 4. Save artifacts
    print("Saving model artifacts...")
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, os.path.join('models', 'student_model.pkl'))
    joblib.dump(scaler, os.path.join('models', 'scaler.pkl'))
    joblib.dump(mappings, os.path.join('models', 'label_mappings.pkl'))
    joblib.dump(list(df_processed.drop('grade_band', axis=1).columns), os.path.join('models', 'feature_names.pkl'))
    
    # 5. Save a confusion matrix plot
    plt.figure(figsize=(8, 6))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    os.makedirs('outputs', exist_ok=True)
    plt.savefig(os.path.join('outputs', 'confusion_matrix.png'))
    print("Training complete. Artifacts saved in 'models/' and 'outputs/'.")

if __name__ == "__main__":
    train_model()
