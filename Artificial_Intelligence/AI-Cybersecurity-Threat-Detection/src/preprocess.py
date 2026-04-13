import pandas as pd
import joblib

def preprocess_data(df, training=True, columns_path="models/columns.pkl"):
    
    # Remove missing values
    df = df.dropna()

    # Remove '.' from label (normal. → normal)
    df['label'] = df['label'].str.replace('.', '', regex=False)

    # Convert label to binary (0 = normal, 1 = attack)
    df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

    # Convert categorical columns into numeric
    categorical_cols = ['protocol_type', 'service', 'flag']
    df = pd.get_dummies(df, columns=categorical_cols)

    if training:
        # Save column structure during training
        joblib.dump(df.columns, columns_path)
    else:
        # Load saved columns and align test data
        saved_columns = joblib.load(columns_path)
        df = df.reindex(columns=saved_columns, fill_value=0)

    return df