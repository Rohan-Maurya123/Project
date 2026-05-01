import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create outputs directory if it doesn't exist
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# Load data
data = pd.read_csv("data/dataset.csv")

print("Data Info:")
print(data.info())

print("\nDescriptive Statistics:")
print(data.describe())

# 1. Performance Distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x="Performance", order=["Low", "Medium", "High"])
plt.title("Performance Distribution")
plt.savefig("outputs/performance_dist.png")
plt.close()

# 2. Correlation Heatmap (numeric only)
plt.figure(figsize=(12, 8))
numeric_data = data.select_dtypes(include=['int64', 'float64'])
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

# 3. Experience vs Performance
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="Performance", y="Experience", order=["Low", "Medium", "High"])
plt.title("Experience vs Performance")
plt.savefig("outputs/experience_vs_performance.png")
plt.close()

# 4. Feedback Score vs Performance
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="Performance", y="Feedback_Score", order=["Low", "Medium", "High"])
plt.title("Feedback Score vs Performance")
plt.savefig("outputs/feedback_vs_performance.png")
plt.close()

print("\nEDA complete. Plots saved to outputs/")
