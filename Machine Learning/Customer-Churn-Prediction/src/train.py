import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
import joblib
from preprocess import load_data

# Ensure models directory exists
os.makedirs("models", exist_ok=True)

df = load_data("data/telco_churn.csv")

# Feature Engineering: 
# 1. Count total services used
service_cols = [
    "PhoneService", "MultipleLines", "InternetService", 
    "OnlineSecurity", "OnlineBackup", "DeviceProtection", 
    "TechSupport", "StreamingTV", "StreamingMovies"
]
df["TotalServices"] = df[service_cols].apply(lambda x: x.str.contains("Yes").sum(), axis=1)

# 2. Avg monthly charge per tenure (avoid division by zero)
df["AvgMonthlyPerTenure"] = df["MonthlyCharges"] / (df["tenure"] + 1)

# Identify feature types
numeric_features = ["tenure", "MonthlyCharges", "TotalCharges", "TotalServices", "AvgMonthlyPerTenure"]
categorical_features = [
    "gender", "SeniorCitizen", "Partner", "Dependents", 
    "PhoneService", "MultipleLines", "InternetService", 
    "OnlineSecurity", "OnlineBackup", "DeviceProtection", 
    "TechSupport", "StreamingTV", "StreamingMovies", 
    "Contract", "PaperlessBilling", "PaymentMethod"
]

X = df[numeric_features + categorical_features]
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Create preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ]
)

# Optimize XGBoost for higher accuracy
model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", XGBClassifier(
            eval_metric='logloss',
            learning_rate=0.05,
            max_depth=4,
            n_estimators=500,
            subsample=0.8,
            colsample_bytree=0.8,
            gamma=1,
            min_child_weight=1,
            use_label_encoder=False,
            random_state=42
        )),
    ]
)

model_pipeline.fit(X_train, y_train)

# Save the full pipeline and metadata
joblib.dump(model_pipeline, "models/churn_pipeline.pkl")

# Save categories for the UI
categories = {feat: df[feat].unique().tolist() for feat in categorical_features}
joblib.dump(categories, "models/categories.pkl")
joblib.dump(numeric_features + categorical_features, "models/features_list.pkl")

acc = model_pipeline.score(X_test, y_test)
print("Pipeline optimized and saved.")
print("Accuracy on test set:", acc)

with open("accuracy_log.txt", "w") as f:
    f.write(f"Accuracy: {acc}\n")