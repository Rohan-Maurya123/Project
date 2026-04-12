import os

def menu():
    print("\n============================")
    print(" AI MEDICAL IMAGE SYSTEM")
    print("============================")
    print("1. Train Model")
    print("2. Predict Image")
    print("3. Exit")
    print("============================")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        print("\n Training Model...\n")
        os.system("python -m src.train")

    elif choice == "2":
        print("\n Running Prediction...\n")
        os.system("python src/predict.py")

    elif choice == "3":
        print(" Exiting...")
        break

    else:
        print(" Invalid choice")