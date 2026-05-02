def preprocess_data(df):
    # No missing values in this dataset usually
    # But still safe check
    
    df = df.dropna()
    
    X = df.drop("MEDV", axis=1)
    y = df["MEDV"]
    
    return X, y