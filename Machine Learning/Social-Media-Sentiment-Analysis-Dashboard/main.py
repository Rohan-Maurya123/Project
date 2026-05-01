import os
import sys
import subprocess

def train():
    """
    Runs the training script.
    """
    print("Starting model training...")
    # Add project root to path so src can be imported
    sys.path.append(os.getcwd())
    from src.train import train_sentiment_model
    
    data_path = 'data/training.1600000.processed.noemoticon.csv'
    if not os.path.exists(data_path):
        print(f"Warning: Dataset not found at {data_path}. Training with sample data.")
        data_path = None
        
    train_sentiment_model(data_path)
    print("Training completed successfully.")

def run_app():
    """
    Runs the Streamlit app.
    """
    print("Starting Streamlit app...")
    # Use python -m streamlit to ensure it uses the current environment's streamlit
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app/app.py"])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "train":
            train()
        elif command == "app":
            run_app()
        else:
            print("Unknown command. Use 'train' or 'app'.")
    else:
        # Default behavior: show help
        print("Social Media Sentiment Analysis Dashboard")
        print("Usage:")
        print("  python main.py train    - Train the sentiment model")
        print("  python main.py app      - Start the Streamlit dashboard")
