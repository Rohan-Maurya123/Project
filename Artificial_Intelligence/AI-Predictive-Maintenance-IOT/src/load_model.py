import joblib

def load_model():
    model = joblib.load("models/model.pkl")
    print(" Model loaded successfully")
    return model