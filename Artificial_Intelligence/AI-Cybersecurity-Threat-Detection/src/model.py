from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib

def train_model(df):
    X = df.drop('label', axis=1)
    y = df['label']

    print("Label Distribution in original data:")
    print(y.value_counts())

    # -------------------------------
    # SPLIT DATA FIRST (To avoid leakage)
    # -------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # -------------------------------
    # BALANCING DATA (ONLY ON TRAINING SET)
    # -------------------------------
    from sklearn.utils import resample
    import pandas as pd

    train_combined = pd.concat([X_train, y_train], axis=1)
    normal = train_combined[train_combined['label'] == 0]
    attack = train_combined[train_combined['label'] == 1]

    print(f"Original training distribution: Normal={len(normal)}, Attack={len(attack)}")

    # Upsample attack data in training set only
    attack_upsampled = resample(
        attack,
        replace=True,
        n_samples=len(normal),
        random_state=42
    )

    df_train_balanced = pd.concat([normal, attack_upsampled])
    X_train_balanced = df_train_balanced.drop('label', axis=1)
    y_train_balanced = df_train_balanced['label']

    print("Balanced training distribution:")
    print(y_train_balanced.value_counts())

    # -------------------------------
    # TRAIN MODEL (With Regularization)
    # -------------------------------
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,        # 🔥 Added to prevent overfitting
        min_samples_leaf=5,  # 🔥 Added to prevent overfitting
        random_state=42,
        class_weight='balanced' # 🔥 Added to handle imbalance more naturally
    )

    model.fit(X_train_balanced, y_train_balanced)

    joblib.dump(model, "models/model.pkl")

    # -------------------------------
    # EVALUATION
    # -------------------------------
    y_pred = model.predict(X_test)

    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    return model