import pandas as pd
import os
import sys

def load_data(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        print(f"Warning: {path} is missing or empty. Attempting to generate data...")
        try:
            from src.data_simulation import generate_climate_data
            generate_climate_data()
        except ImportError:
            print("Error: Could not import data_simulation. Please run it manually.")
            sys.exit(1)
            
    try:
        df = pd.read_csv(path)
        return df
    except pd.errors.EmptyDataError:
        print(f"Error: {path} is empty even after attempted generation.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)