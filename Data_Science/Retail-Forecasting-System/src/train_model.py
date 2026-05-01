import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import LabelEncoder
import joblib
import os

def create_advanced_features(df):
    """
    Creates time-series features for forecasting with lags and rolling windows.
    """
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['product_id', 'date'])
    
    # Time features
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.weekday
    df['is_weekend'] = df['weekday'].isin([5, 6]).astype(int)
    
    # Encode product_id
    le = LabelEncoder()
    df['product_id_encoded'] = le.fit_transform(df['product_id'])
    
    # Lag features (Sales from previous days)
    for lag in [1, 7]:
        df[f'sales_lag_{lag}'] = df.groupby('product_id')['sales'].shift(lag)
    
    # Rolling features (Moving averages)
    for window in [7]:
        df[f'sales_rolling_mean_{window}'] = df.groupby('product_id')['sales'].transform(
            lambda x: x.shift(1).rolling(window=window).mean()
        )
        
    # Drop rows with NaN created by lagging
    df = df.dropna()
    return df, le

def train_forecasting_model():
    # Load data
    data_path = "data/sales_data.csv"
    if not os.path.exists(data_path):
        print(f"Data not found at {data_path}. Please run main.py first.")
        return

    df = pd.read_csv(data_path)
    
    # Feature engineering
    print("Creating advanced features...")
    df_features, le = create_advanced_features(df)
    
    # Select features for training
    features = [
        'price', 'is_promotion', 'day', 'month', 'weekday', 'is_weekend',
        'product_id_encoded', 'sales_lag_1', 'sales_lag_7',
        'sales_rolling_mean_7'
    ]
    target = 'sales'
    
    X = df_features[features]
    y = df_features[target]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    # Initialize and train model
    print("Training Random Forest model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    model.fit(X_train, y_train)
    
    # Evaluate
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    
    print(f"Model Training Complete.")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    
    # Save model, features, and encoder
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/sales_forecasting_model.pkl")
    joblib.dump(features, "models/feature_columns.pkl")
    joblib.dump(le, "models/product_encoder.pkl")
    print("Model and assets saved to models/")

if __name__ == "__main__":
    print("Starting model training script...")
    train_forecasting_model()
    print("Script finished.")
