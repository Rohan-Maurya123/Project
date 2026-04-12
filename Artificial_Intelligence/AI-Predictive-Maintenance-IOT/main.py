from src.data_loader import load_data
from src.preprocess import create_labels, prepare_features
from src.train import train_model
from src.predict import evaluate
from src.simulate_iot import simulate_iot
from src.load_model import load_model   

print("🔧 AI Predictive Maintenance System")

choice = input("Enter 1 for TRAIN or 2 for SIMULATION: ")


# TRAIN MODE

if choice == "1":
    # Step 1: Load data
    df = load_data()

    # Step 2: Create labels
    df = create_labels(df)

    # Step 3: Prepare features
    X_train, X_test, y_train, y_test = prepare_features(df)

    # Step 4: Train model (and save)
    model = train_model(X_train, y_train)

    # Step 5: Evaluate
    evaluate(model, X_test, y_test)



# SIMULATION MODE

elif choice == "2":
    # Step 1: Load data
    df = load_data()

    # Step 2: Create labels
    df = create_labels(df)

    # Step 3: Load trained model
    model = load_model()

    # Step 4: Simulate IoT system
    simulate_iot(model, df)


# INVALID INPUT
else:
    print(" Invalid input. Please enter 1 or 2.")