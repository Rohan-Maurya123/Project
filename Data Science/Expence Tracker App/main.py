import os
import subprocess
import sys
from src.data_generator import generate_data
from src.data_cleaning import clean_data
from src.analysis import analyze_data, generate_insights

def run_pipeline():
    print("Starting Expense Tracker Pipeline...")
    
    # 1. Generate Data
    print("\nStep 1: Generating synthetic data...")
    generate_data()
    
    # 2. Clean Data
    print("\nStep 2: Cleaning and engineering features...")
    clean_data()
    
    # 3. Analyze Data (Optional CLI preview)
    print("\nStep 3: Running initial analysis...")
    metrics = analyze_data()
    if metrics:
        insights = generate_insights(metrics)
        print("\nInsights:")
        for insight in insights:
            print(f"- {insight}")
    
    print("\nPipeline Complete!")
    print("\nTo launch the dashboard, run:")
    print("streamlit run app.py")

if __name__ == "__main__":
    run_pipeline()
