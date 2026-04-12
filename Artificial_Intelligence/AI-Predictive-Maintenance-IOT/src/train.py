from sklearn.ensemble import RandomForestClassifier
import joblib
def train_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    print("Model Trained Successfully")

   
    joblib.dump(model, "models/model.pkl")

    print("✅ Model trained & saved successfully")

    return model