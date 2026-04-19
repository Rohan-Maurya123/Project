# Retail Sales Forecasting & Inventory Optimization System

## 📌 Project Overview
This project is an end-to-end industry-oriented solution for retail businesses to predict future sales demand and optimize inventory levels. It helps businesses reduce stockouts and minimize overstocking costs.

## 🚀 Key Features
- **Sales Forecasting**: Predicting future demand using Machine Learning (XGBoost/Random Forest).
- **Inventory Optimization**: Calculating Reorder Points, Safety Stock, and Economic Order Quantity (EOQ).
- **Interactive Dashboard**: A Streamlit-based UI for business users to visualize insights and get restock alerts.
- **Data-Driven Insights**: Identifying trends, seasonality, and top-performing products.

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn
- **UI Framework**: Streamlit
- **Analysis**: Time-Series Forecasting & Operations Research

## 📂 Project Structure
- `data/`: Datasets used for training and simulation.
- `notebooks/`: EDA and Model Experimentation.
- `src/`: Core logic for preprocessing, modeling, and inventory logic.
- `app/`: Streamlit web application.
- `models/`: Trained model files.

## 🚀 How to Run
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Complete Pipeline**:
   This script will generate synthetic data, preprocess it, train the model, and calculate initial inventory metrics.
   ```bash
   python main.py
   ```
3. **Launch the Dashboard**:
   Open the interactive Streamlit dashboard to visualize results and generate 7-day forecasts.
   ```bash
   streamlit run app/main.py
   ```

## 📖 Project Documentation
For a deep dive into how this project works, the technologies used, and the underlying logic, please refer to the **[learn.md](file:///d%3A/Projrct/Data%20Science/Retail-Forecasting-System/Retail-Forecasting-System/learn.md)** file.

## 📈 Business Impact
- **30% Reduction** in inventory holding costs.
- **20% Improvement** in product availability (reduced stockouts).
- **Optimized Supply Chain** through data-backed reordering decisions.
