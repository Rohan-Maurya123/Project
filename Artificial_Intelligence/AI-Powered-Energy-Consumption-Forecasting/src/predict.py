import joblib
from src.preprocess import load_and_clean, get_features

def predict():

    model = joblib.load("models/model.pkl")

    df = load_and_clean("data/energy.csv")
    X, y = get_features(df)

    y_pred = model.predict(X)

    return y, y_pred