import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os

def load_data(file_path):
    """Load the UCI dataset."""
    return pd.read_csv(file_path, sep=';')

def preprocess_data(df):
    """Clean and transform the data."""
    # Handle missing values if any (UCI dataset is usually clean)
    df = df.dropna()

    # Feature Engineering: Create a 'grade_band' target for classification
    # G3 is the final grade (0-20)
    # Band: Fail (0-9), Pass (10-20)
    df['grade_band'] = df['G3'].apply(lambda x: 1 if x >= 10 else 0)
    
    # Drop G1, G2 as they are too highly correlated with G3 (leaking info)
    # But for a realistic simulation, we might keep them or drop them. 
    # Let's drop them for a more challenging prediction based on other factors.
    df = df.drop(['G1', 'G2', 'G3'], axis=1)

    # Encode categorical variables
    le = LabelEncoder()
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    label_mappings = {}
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
        label_mappings[col] = dict(zip(le.classes_, le.transform(le.classes_)))
    
    return df, label_mappings

def get_train_test_split(df, target_col='grade_band'):
    """Split data into train and test sets."""
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

if __name__ == "__main__":
    # Example usage
    data_path = os.path.join('data', 'student-mat.csv')
    df = load_data(data_path)
    df_processed, mappings = preprocess_data(df)
    print(f"Processed data shape: {df_processed.shape}")
    print("Sample mappings:", list(mappings.items())[:2])
