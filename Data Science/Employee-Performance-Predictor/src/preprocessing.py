import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(data, is_training=True, encoders=None):
    data = data.copy()

    # Drop Employee_ID as it's not a feature
    if "Employee_ID" in data.columns:
        data = data.drop("Employee_ID", axis=1)

    # Feature Engineering
    # 1. Projects per year of experience (adding small value to denominator to avoid division by zero)
    data["Projects_Per_Year"] = data["Projects"] / (data["Experience"] + 1)
    # 2. Training intensity
    data["Training_Intensity"] = data["Training_Hours"] / (data["Age"] - 20)
    
    # Handle Department encoding
    if is_training:
        le_dept = LabelEncoder()
        data["Department"] = le_dept.fit_transform(data["Department"])
        encoders = {"le_dept": le_dept}
    else:
        if encoders and "le_dept" in encoders:
            data["Department"] = encoders["le_dept"].transform(data["Department"])
        else:
            raise ValueError("Encoders must be provided for inference")

    # Map Performance to numeric if it exists (only during training/eval, not during prediction on new data)
    if "Performance" in data.columns:
        data["Performance"] = data["Performance"].map({
            "Low": 0,
            "Medium": 1,
            "High": 2
        })
        y = data["Performance"]
        X = data.drop("Performance", axis=1)
    else:
        X = data
        y = None

    # Scaling numeric features
    if is_training:
        scaler = StandardScaler()
        X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
        encoders["scaler"] = scaler
        return X_scaled, y, encoders
    else:
        if encoders and "scaler" in encoders:
            X_scaled = pd.DataFrame(encoders["scaler"].transform(X), columns=X.columns)
            return X_scaled
        else:
            raise ValueError("Scaler must be provided for inference")