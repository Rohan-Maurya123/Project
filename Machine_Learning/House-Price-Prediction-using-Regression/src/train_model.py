from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Save model
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    return model, X_test, y_test