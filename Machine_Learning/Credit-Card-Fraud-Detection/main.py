from sklearn.model_selection import train_test_split

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import train_model
from src.evaluate import evaluate_model

def main():
    # Load data
    df = load_data("data/creditcard.csv")

    # Preprocess
    X, y = preprocess_data(df)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train
    model = train_model(X_train, y_train)

    # Evaluate
    evaluate_model(model, X_test, y_test)

    print("✅ Model trained & saved successfully!")

if __name__ == "__main__":
    main()