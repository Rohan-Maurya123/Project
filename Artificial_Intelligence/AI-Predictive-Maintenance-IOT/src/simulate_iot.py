import time
import pandas as pd

def simulate_iot(model, df):
    print("\n🔄 Starting IoT Simulation...\n")

    # Select all sensor columns
    sensor_cols = [col for col in df.columns if 'sensor' in col]

    sample_data = df[df['unit'] == 1].head(200)


    for index, row in sample_data.iterrows():

   
        sensor_values = pd.DataFrame(
            [row[sensor_cols].values],
            columns=sensor_cols
        )

        # Predict
        prediction = model.predict(sensor_values)[0]

        # Print basic info
        print(f"Cycle: {int(row['cycle'])}")
        print(f"Sensor Data (first 3): {sensor_values.values.flatten()[:3]}")

        # Output result
        if prediction == 1:
            print("⚠️ ALERT: Machine Failure Predicted!\n")
        else:
            print("✅ Machine Running Normally\n")

        time.sleep(1)