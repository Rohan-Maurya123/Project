import pandas as pd
import numpy as np

def generate_data(n=1000):
    np.random.seed(42)

    data = pd.DataFrame({
        "Employee_ID": range(1, n + 1),
        "Age": np.random.randint(22, 60, n),
        "Experience": np.random.randint(1, 25, n),
        "Salary": np.random.randint(30000, 150000, n),
        "Training_Hours": np.random.randint(10, 120, n),
        "Projects": np.random.randint(1, 15, n),
        "Attendance": np.random.randint(70, 100, n),
        "Feedback_Score": np.random.randint(1, 11, n),
        "Department": np.random.choice(["IT", "HR", "Sales", "Marketing", "Finance"], n)
    })

    def assign_performance(row):
        # Base score from features
        score = (
            row["Experience"] * 2.5 +
            row["Training_Hours"] * 0.5 +
            row["Projects"] * 4.0 +
            row["Attendance"] * 0.8 +
            row["Feedback_Score"] * 5.0
        )
        
        # Add some randomness/noise
        score += np.random.normal(0, 10)

        if score > 160:
            return "High"
        elif score > 100:
            return "Medium"
        else:
            return "Low"

    data["Performance"] = data.apply(assign_performance, axis=1)
    
    # Save to CSV
    data.to_csv("data/dataset.csv", index=False)
    print("Dataset generated and saved to data/dataset.csv")

    return data