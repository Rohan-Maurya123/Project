import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from preprocess import load_data

# Load pipeline
pipeline = joblib.load("models/churn_pipeline.pkl")
features_list = joblib.load("models/features_list.pkl")

df = load_data("data/telco_churn.csv")

# Feature Engineering in Evaluation
service_cols = [
    "PhoneService", "MultipleLines", "InternetService", 
    "OnlineSecurity", "OnlineBackup", "DeviceProtection", 
    "TechSupport", "StreamingTV", "StreamingMovies"
]
df["TotalServices"] = df[service_cols].apply(lambda x: x.str.contains("Yes").sum(), axis=1)
df["AvgMonthlyPerTenure"] = df["MonthlyCharges"] / (df["tenure"] + 1)

# Ensure same features are used
X = df[features_list]
y = df["Churn"]

y_pred = pipeline.predict(X)

print("--- Evaluation Results ---")
print("Accuracy:", accuracy_score(y, y_pred))
print("\nClassification Report:\n", classification_report(y, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y, y_pred))