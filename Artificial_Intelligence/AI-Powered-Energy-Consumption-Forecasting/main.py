from src.train import train_model
from src.predict import predict

print("\n=== ENERGY FORECAST SYSTEM ===")
print("1. Train Model")

choice = input("Enter 1 To Confirm : ")

if choice == "1":
    train_model()


else:
    print("Please Enter 1 to Make Sure You Want To Run Train Model ")