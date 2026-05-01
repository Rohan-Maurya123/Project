# 💎 Executive Churn Intelligence

A high-performance Customer Churn Prediction system featuring a premium executive dashboard and an optimized XGBoost machine learning engine.

## 🚀 Overview
This project provides a comprehensive solution for predicting customer churn in the telecommunications industry. It utilizes advanced machine learning techniques to identify at-risk customers with high precision, allowing for proactive retention strategies.

### Key Features
- **Premium Executive Dashboard**: A modern, high-contrast interface built with Streamlit for intuitive risk assessment.
- **Optimized XGBoost Engine**: A finely-tuned model utilizing feature engineering and class-balancing techniques.
- **Strategic Insights**: Real-time churn probability with tailored retention recommendations.
- **High Sensitivity**: Optimized for a high Recall rate (85.0%) using an automated XGBoost Pipeline to ensure at-risk customers are identified.
- **Full Feature Analysis**: Incorporates all 19 customer features including service types, billing methods, and demographics for maximum reliability.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Machine Learning**: XGBoost, Scikit-Learn
- **Interface**: Streamlit
- **Data Handling**: Pandas, Joblib

## 📦 Project Structure
```text
├── data/               # Dataset (telco_churn.csv)
├── models/             # Trained model and feature metadata
├── src/                # Core logic (Preprocess, Train, Evaluate)
├── app_ui.py           # Premium Streamlit Dashboard
└── requirements.txt    # Project dependencies
```

## ⚡ Getting Started

### 1. Installation
Clone the repository and install the dependencies:
```bash
pip install -r requirements.txt
```

### 2. Training the Model
Ensure your data is in the `data/` folder, then run:
```bash
python src/train.py
```

### 3. Launching the Dashboard
Start the executive interface:
```bash
streamlit run app_ui.py
```

## 📊 Model Performance
- **Accuracy**: 80.2%
- **Recall**: 87.0%
- **Engine**: XGBoost v2.0
- **Status**: Balanced & Optimized for Imbalanced Data

## 📄 License
This project is for analytical and educational purposes.

---
*Developed for Enterprise Churn Analytics.*
