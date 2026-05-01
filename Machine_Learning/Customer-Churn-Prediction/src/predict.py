import joblib
import pandas as pd

# Load pipeline
pipeline = joblib.load("models/churn_pipeline.pkl")

def predict(data_dict):
    """
    Predict churn probability for a given customer profile.
    data_dict: dictionary containing all feature values.
    """
    df = pd.DataFrame([data_dict])
    prediction = pipeline.predict(df)[0]
    probability = pipeline.predict_proba(df)[0][1]
    return prediction, probability