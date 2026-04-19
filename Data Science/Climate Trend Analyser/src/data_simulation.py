import pandas as pd
import numpy as np

def generate_climate_data():
    # Set start date to 2021 to make the data more relevant to 2026
    # 2000 periods (approx 5.5 years) will take us into mid-2026
    periods = 2000
    dates = pd.date_range(start="2021-01-01", periods=periods)
    temp = 20 + np.random.normal(0,1,periods) + np.linspace(0,2,periods)

    df = pd.DataFrame({
        "Date": dates,
        "Temperature": temp
    })

    df.to_csv("data/climate_data.csv", index=False)
    print("Synthetic dataset created at data/climate_data.csv")

if __name__ == "__main__":
    generate_climate_data()