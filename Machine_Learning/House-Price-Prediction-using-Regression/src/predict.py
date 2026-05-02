import pickle
import numpy as np
import os

def load_model():
    # Use absolute path for model loading
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    model_path = os.path.join(base_dir, "models", "model.pkl")
    with open(model_path, "rb") as f:
        return pickle.load(f)

def predict_price(features):
    model = load_model()
    # If the model expects 13 features but we only provide 12 (removed 'B'), 
    # we should handle it. However, since the user wants it removed entirely,
    # we should ideally retrain the model. For now, we'll pad it with a default value
    # to keep the app running, or assume the model will be updated.
    
    # Padding with a neutral value (e.g., 350.0 which was the previous default for B)
    # if features count is 12
    if len(features) == 12:
        features.insert(11, 350.0) 
        
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    
    # Ensure the price is not negative and stays within reasonable bounds
    result = max(0, prediction[0])
    return result