# AI-Powered Predictive Maintenance for IoT Devices

---

##  Overview

This project builds an AI system that predicts machine failures using IoT sensor data.
It uses the NASA Turbofan Engine Degradation Dataset to simulate real-world industrial predictive maintenance.

---

##  Problem Statement

In industries, machines are often repaired only after failure (reactive maintenance), which leads to:

* High downtime
* Increased cost
* Production loss

This project solves this problem by predicting failures **before they happen**.

---

## Industry Relevance

Predictive maintenance is used in:

* Manufacturing plants
* Power plants
* Automotive industry
* Aviation industry

Companies like Siemens, GE, and Tesla use similar systems to reduce downtime and improve efficiency.

---

## Features

* Machine failure prediction using Machine Learning
* NASA dataset-based simulation
* Time-series lifecycle analysis
* Confusion matrix evaluation
* Real-time IoT-style prediction

---

##  Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib

---

## Dataset

* NASA Turbofan Engine Degradation Dataset (FD001)
* Contains:

  * Engine ID (unit)
  * Time cycles
  * Sensor readings

---

## Project Workflow

1. Load dataset
2. Create Remaining Useful Life (RUL)
3. Convert RUL into failure labels
4. Train machine learning model
5. Evaluate model performance
6. Simulate real-time IoT prediction

---

##  Project Structure

AI-Predictive-Maintenance-IoT/
│
├── data/
│   └── train_FD001.txt
|
├── docs/
│   └── .gitkeep
|
├── images/
│   ├── confusion_matrix.png
│   ├── simulation_output.png
|
├── models/
│   └── model.pkl
|
├── notebooks/
|
├── outputs/
│   ├── simulation_output_01.png
│   ├── simulation_output_02.png
|
├── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   ├── simulate_iot.py
│   ├── load_model.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore


---

## How to Run the Project

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 2: Train the Model

```bash
python main.py
```

Enter:

```
1
```

---

### Step 3: Run Simulation

```bash
python main.py
```

Enter:

```
2
```

---

## Results

### 🔹 Model Performance

* Accuracy: ~96%
* Model: Random Forest Classifier

---

### 🔹 Confusion Matrix

![Confusion Matrix](images/confusion_matrix.png)

---

### Simulation Output

![Simulation Output](images/simulation_output.png)

---

##  Key Learning Outcomes

* Predictive maintenance using AI
* Time-series data understanding
* Machine learning model training
* IoT system simulation
* Model saving and loading (joblib)

---

## Future Improvements

* Add Flask API for real-time predictions
* Build dashboard using Streamlit
* Integrate real IoT sensors (Raspberry Pi)

---

##  Author

Rohan Maurya

---

## If you like this project

Give it a ⭐ on GitHub!
