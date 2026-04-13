from src.data_loader import load_data
from src.preprocess import preprocess_data
import joblib

# Load test data
test_df = load_data("data/test.csv")

print("Raw Test Shape:", test_df.shape)

# Preprocess (IMPORTANT: training=False)
test_df = preprocess_data(test_df, training=False)

print("Processed Test Shape:", test_df.shape)

# Load model
model = joblib.load("models/model.pkl")

# Separate features
X_test = test_df.drop('label', axis=1)
y_test = test_df['label']

# Predict
predictions = model.predict(X_test)

print("Sample Predictions:", predictions[:10])

# Summary
num_threats = sum(predictions)
total = len(predictions)
summary = f"Results: {num_threats} threats detected out of {total} samples."
print(summary)

# Classification Report
from sklearn.metrics import classification_report, confusion_matrix
report = f"\nConfusion Matrix:\n{confusion_matrix(y_test, predictions)}\n\nClassification Report:\n{classification_report(y_test, predictions)}"
print(report)

# Save results to file for verification
with open("test_results.txt", "w") as f:
    f.write(summary + "\n" + report)