import subprocess
import sys

def run_pipeline():
    print("--- Starting ML Pipeline ---")
    
    # Train
    print("\n1. Training Model...")
    subprocess.run([sys.executable, "src/train.py"])
    
    # Evaluate
    print("\n2. Evaluating Model...")
    subprocess.run([sys.executable, "src/evaluate.py"])
    
    print("\n--- Pipeline Complete ---")
    print("Run 'streamlit run app_ui.py' to launch the dashboard.")

if __name__ == "__main__":
    run_pipeline()