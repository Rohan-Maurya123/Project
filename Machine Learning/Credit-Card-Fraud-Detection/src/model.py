from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
import joblib

def train_model(X_train, y_train):
    sm = SMOTE(random_state=42)
    X_res, y_res = sm.fit_resample(X_train, y_train)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_res, y_res)

    joblib.dump(model, "models/fraud_model.pkl")

    return model


def load_model():
    return joblib.load("models/fraud_model.pkl")