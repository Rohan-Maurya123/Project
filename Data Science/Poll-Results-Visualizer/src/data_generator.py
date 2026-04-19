import pandas as pd
import numpy as np

def generate_data(n=500, save_path="data/poll_data.csv"):
    np.random.seed(42)

    data = pd.DataFrame({
        "Respondent_ID": range(1, n+1),
        "Region": np.random.choice(["North", "South", "East", "West"], n),
        "Age_Group": np.random.choice(["18-25", "26-35", "36-50"], n),
        "Question": "Which product do you prefer?",
        "Response": np.random.choice(
            ["Product A", "Product B", "Product C"],
            n,
            p=[0.5, 0.3, 0.2]
        ),
        "Date": pd.date_range(start="2024-01-01", periods=n, freq='D')
    })

    data.to_csv(save_path, index=False)
    return data