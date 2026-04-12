#  AI-Powered Energy Consumption Forecasting System

##  Overview
This project is a Machine Learning-based system that forecasts household electricity consumption using historical time-series energy usage data. It simulates real-world smart energy systems used in smart cities, power grids, and energy optimization platforms.

The system analyzes past electricity usage patterns and predicts future consumption to help improve energy efficiency and planning.

---

## Problem Statement
Electricity demand changes over time based on usage behavior, time of day, and seasonal patterns. Without prediction systems, energy providers face power overloads, energy wastage, and inefficient distribution.

This project solves this problem by forecasting energy consumption using AI and machine learning techniques.

---

## Solution Approach
1. Load time-series energy dataset  
2. Clean and preprocess data  
3. Perform feature engineering (time-based + lag features)  
4. Train machine learning models  
5. Evaluate performance  
6. Visualize predictions  
7. Deploy using Streamlit dashboard  

---

## Dataset
The dataset contains household electricity usage records:

- Date → Date of measurement  
- Time → Time of measurement  
- Global_active_power →  Electricity consumption (target variable)

---

##  Tech Stack
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  
- Joblib  

---

##  Machine Learning Models

### Baseline Model
- Linear Regression
- Used for performance comparison

### Final Model
- Random Forest Regressor
- Captures non-linear patterns and improves accuracy

---

##  Performance

- Baseline Model R²: ~0.92  
- Random Forest R²: ~0.93+  
- RMSE: Low error range indicating good prediction accuracy  

---

##  Features Used
- Hour of day  
- Day, Month  
- Weekday  
- Lag features (previous values)  
- Rolling mean (trend detection)  

---

##  Project Structure
AI-Powered-Energy-Forecasting/
│
├── data/
├── models/
├── outputs/
├── src/
│   ├── preprocess.py
│   ├── train.py
│
├── app.py
├── requirements.txt
├── README.md

---

##  How to Run

### Install dependencies
pip install -r requirements.txt

### Train model
python -m src.train

### Run dashboard
streamlit run app.py

---

##  Outputs
- Actual vs Predicted graphs  
- RMSE & R² evaluation  
- Saved model file  
- Prediction CSV results  

---

##  Key Learnings
- Time-series forecasting  
- Feature engineering  
- Model evaluation  
- Real-world ML pipeline design  
- Streamlit dashboard development  

---

##  Future Improvements
- LSTM deep learning model  
- Real-time energy prediction system  
- Cloud deployment  
- Multi-household forecasting  
- Smart alert system for high usage  

---

##  Author
Rohan Maurya

---

##  Conclusion
This project demonstrates an end-to-end machine learning system for forecasting household energy consumption, simulating real-world smart energy management applications.