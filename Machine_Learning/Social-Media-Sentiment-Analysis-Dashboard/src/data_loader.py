import pandas as pd
import os

def load_data(file_path):
    """
    Loads the Twitter Sentiment Analysis dataset.
    If the file doesn't exist, it creates a small synthetic dataset for demonstration.
    """
    if os.path.exists(file_path):
        print(f"Loading data from {file_path}...")
        # Sentiment140 format: target, ids, date, flag, user, text
        columns = ['target', 'id', 'date', 'flag', 'user', 'text']
        df = pd.read_csv(file_path, encoding='ISO-8859-1', names=columns)
        return df
    else:
        print(f"File {file_path} not found. Creating synthetic dataset...")
        data = {
            'target': [0, 0, 4, 4, 0, 4, 0, 4, 0, 4],
            'text': [
                "I am so sad today, feeling blue.",
                "This product is terrible, I hate it!",
                "I love this new phone, it's amazing!",
                "Great weather today, feeling happy!",
                "I'm very disappointed with the service.",
                "The food was delicious and the staff were friendly.",
                "Worst experience ever, never coming back.",
                "Awesome work! Keep it up.",
                "I'm feeling really stressed and tired.",
                "Such a beautiful day for a walk!"
            ]
        }
        df = pd.DataFrame(data)
        # Map 4 to 1 for simplicity (0=Negative, 1=Positive)
        df['target'] = df['target'].replace(4, 1)
        return df

if __name__ == "__main__":
    # Test loading
    df = load_data('data/training.1600000.processed.noemoticon.csv')
    print(df.head())
