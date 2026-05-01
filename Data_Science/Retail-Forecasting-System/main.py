import os
import pandas as pd
from src.data_generator import generate_data
from src.preprocess import load_data
from src.feature_engineering import create_features
from src.forecasting import train_model, predict
from src.inventory import inventory_logic
from src.visualization import plot_sales

# Ensure directories exist
os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
os.makedirs("models", exist_ok=True)

print("Generating synthetic data...")
df = generate_data()
df.to_csv("data/sales_data.csv", index=False)

print("Preprocessing data...")
df = load_data("data/sales_data.csv")
df = create_features(df)

print("Training model...")
model = train_model(df)

print("Making forecasts...")
df = predict(model, df)

print("Optimizing inventory...")
df = inventory_logic(df)

print("Saving results...")
df.to_csv("outputs/final_output.csv", index=False)

print("Generating plots...")
plot_sales(df)

print("Project executed successfully!")