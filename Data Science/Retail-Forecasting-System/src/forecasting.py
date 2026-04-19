import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import os

def train_model(df):
    """
    Trains a Random Forest model on sales data.
    """
    # Feature engineering (already done in create_features, but let's be sure)
    df = df.copy()
    
    # Encode categorical features
    le_product = LabelEncoder()
    df['product_id_encoded'] = le_product.fit_transform(df['product_id'])
    
    features = ['day', 'month', 'weekday', 'product_id_encoded', 'is_promotion']
    X = df[features]
    y = df['sales']

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Save model and encoder
    os.makedirs("models", exist_ok=True)
    import joblib
    joblib.dump(model, "models/sales_forecasting_model.pkl")
    joblib.dump(le_product, "models/product_encoder.pkl")
    
    return model

def predict(model, df):
    """
    Generates forecasts using the trained model.
    """
    df = df.copy()
    
    # Load encoder or re-fit if not found (for simplicity here, we re-fit if needed)
    # In a real app, we'd load the saved encoder.
    le_product = LabelEncoder()
    df['product_id_encoded'] = le_product.fit_transform(df['product_id'])
    
    features = ['day', 'month', 'weekday', 'product_id_encoded', 'is_promotion']
    X = df[features]
    df['forecast'] = model.predict(X)
    return df