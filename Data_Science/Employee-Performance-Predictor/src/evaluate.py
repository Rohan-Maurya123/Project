from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    # Feature Importance
    importances = model.feature_importances_
    feature_importance = pd.DataFrame({
        'Feature': X_test.columns,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)

    return acc, cm, report, feature_importance
