from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.model import train_model

# Load training data
train_df = load_data("data/train.csv")

print("Raw Train Shape:", train_df.shape)

# Preprocess (IMPORTANT: training=True)
train_df = preprocess_data(train_df, training=True)

print("Processed Train Shape:", train_df.shape)

# Train model
model = train_model(train_df)

print("✅ Model Training Completed!")