import subprocess
import sys
import os

def run_project():
    print("--- Student Performance Prediction System ---")
    print("1. Train Model")
    print("2. Start FastAPI Backend")
    print("3. Start Streamlit Frontend")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        subprocess.run([sys.executable, "src/train.py"])
    elif choice == '2':
        print("Starting FastAPI on http://localhost:8000")
        subprocess.run([sys.executable, "src/api.py"])
    elif choice == '3':
        print("Starting Streamlit Dashboard...")
        subprocess.run(["streamlit", "run", "src/dashboard.py"])
    elif choice == '4':
        sys.exit()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    run_project()
