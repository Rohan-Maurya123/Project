import pandas as pd
from datetime import datetime
import os


def save_report(city, temp, humidity, condition, wind, alerts):

    os.makedirs("outputs", exist_ok=True)

    report = {
        "City": [city],
        "Temperature (C)": [temp],
        "Humidity (%)": [humidity],
        "Condition": [condition],
        "Wind Speed (kph)": [wind],
        "Alerts": [", ".join(alerts)],
        "Timestamp": [datetime.now()]
    }

    df = pd.DataFrame(report)

    file_path = "outputs/forecast_report.csv"

    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)

    print("✅ Report Saved Successfully")