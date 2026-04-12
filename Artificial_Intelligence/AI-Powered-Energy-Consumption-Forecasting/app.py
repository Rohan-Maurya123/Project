import streamlit as st
import matplotlib.pyplot as plt
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

from src.preprocess import load_and_clean, get_features, time_split

st.title("⚡ Energy Forecast Dashboard")

model = joblib.load("models/model.pkl")

uploaded_file = st.file_uploader("Upload CSV")

if uploaded_file:

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    df = load_and_clean(uploaded_file)
    X, y = get_features(df)

    
    X_train, X_test, y_train, y_test = time_split(X, y)

    y_pred = model.predict(X_test)

    # METRICS
    rmse = np.sqrt(((y_test - y_pred) ** 2).mean())
    r2 = 1 - (((y_test - y_pred) ** 2).sum() /
              ((y_test - y_test.mean()) ** 2).sum())

    st.write("RMSE:", rmse)
    st.write("R2:", r2)

    # GRAPH
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(y_test.values[:200], label="Actual")
    ax.plot(y_pred[:200], label="Predicted")
    ax.legend()
    ax.grid()

    st.pyplot(fig)

    # SAVE OUTPUTS
    results = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": y_pred
    })

    results.to_csv(f"outputs/result/streamlit_results_{timestamp}.csv", index=False)

    fig.savefig(f"outputs/result/streamlit_graph_{timestamp}.png")
    plt.close(fig)