import os
import joblib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from src.preprocess import load_and_clean, get_features, time_split


def train_model():

    os.makedirs("models", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # LOAD DATA
    df = load_and_clean("data/energy.csv")
    X, y = get_features(df)

    # TIME SPLIT (IMPORTANT)
    X_train, X_test, y_train, y_test = time_split(X, y)

    # ---------------- BASELINE ----------------
    baseline = LinearRegression()
    baseline.fit(X_train, y_train)
    base_pred = baseline.predict(X_test)

    base_rmse = np.sqrt(mean_squared_error(y_test, base_pred))
    base_r2 = r2_score(y_test, base_pred)

    # ---------------- MODEL ----------------
    model = RandomForestRegressor(
        n_estimators=150,
        max_depth=12,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    # PRINT RESULTS
    print("\n========== RESULTS ==========\n")

    print("BASELINE:")
    print("RMSE:", base_rmse)
    print("R2:", base_r2)

    print("\nRANDOM FOREST:")
    print("RMSE:", rmse)
    print("R2:", r2)

    # SAVE MODEL
    joblib.dump(model, "models/model.pkl")

    # SAVE GRAPH
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(y_test.values[:200], label="Actual")
    ax.plot(y_pred[:200], label="Predicted")
    ax.legend()
    ax.grid()

    fig.savefig(f"outputs/train/train_graph_{timestamp}.png")
    plt.show()
    plt.close(fig)

    # SAVE CSV
    results = X_test.copy()
    results["Actual"] = y_test.values
    results["Predicted"] = y_pred

    results.to_csv(f"outputs/train/train_results_{timestamp}.csv", index=False)

    # SAVE REPORT
    with open(f"outputs/train/report_{timestamp}.txt", "w") as f:
        f.write("BASELINE\n")
        f.write(f"RMSE: {base_rmse}\n")
        f.write(f"R2: {base_r2}\n\n")

        f.write("RANDOM FOREST\n")
        f.write(f"RMSE: {rmse}\n")
        f.write(f"R2: {r2}\n")


if __name__ == "__main__":
    train_model()