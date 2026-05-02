from src.load_data import load_data
from src.preprocess import preprocess_data
from src.train_model import train_model
from src.evaluate import evaluate_model

# Load data
df = load_data("data/housing.csv")

# Preprocess
X, y = preprocess_data(df)

# Train
model, X_test, y_test = train_model(X, y)

# Evaluate
mae, r2 = evaluate_model(model, X_test, y_test)

print("MAE:", mae)
print("R2 Score:", r2)