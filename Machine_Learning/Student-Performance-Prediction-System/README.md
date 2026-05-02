# 🎓 Student Performance Prediction System (SPPS)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)](https://streamlit.io/)
[![ML](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange.svg)](https://scikit-learn.org/)

An end-to-end, industry-standard machine learning project designed to predict student academic outcomes and visualize key educational insights through an interactive dashboard.

---

## 🚀 Project Overview
The **Student Performance Prediction System** addresses the critical need in EdTech and educational institutions to identify "at-risk" students early. Using the UCI Student Performance Dataset, this system analyzes over 30 variables—including social habits, family support, and study patterns—to predict a student's final grade band (Pass/Fail) with high precision.

### ✨ Key Features
- **Interactive Dashboard**: Built with Streamlit and Plotly for responsive data exploration.
- **Real-time Inference**: Powered by a FastAPI backend for seamless model consumption.
- **Advanced Visualizations**: Radar charts for lifestyle profiling, Sunburst charts for demographic analysis, and Gauge indicators for prediction confidence.
- **Risk Assessment**: Automated intervention suggestions for flagged students.
- **Modular Architecture**: Clean code structure following production-ready standards.

---

## 🏗️ System Architecture
The system is built with a decoupled architecture to separate concerns:
1.  **Data Pipeline**: Preprocessing and feature engineering of raw UCI data.
2.  **ML Engine**: Random Forest Classifier optimized for tabular categorical data.
3.  **Inference Layer**: FastAPI service providing a RESTful endpoint for predictions.
4.  **UI Layer**: Streamlit dashboard providing a beautiful, animated interface for users.

---

## 📁 Folder Structure
```text
Student-Performance-Prediction/
├── data/           # Raw CSV datasets (UCI Student Performance)
├── models/         # Trained Model, Scaler, and Label Mappings (.pkl)
├── outputs/        # Performance reports and confusion matrices
├── src/            # Core Source Code
│   ├── api.py          # FastAPI Backend Service
│   ├── dashboard.py    # Streamlit Interactive UI
│   ├── preprocess.py   # Data Engineering Pipeline
│   └── train.py        # Model Training Script
├── requirements.txt # Project Dependencies
├── main.py         # Application Entry Point
└── .gitignore      # Git exclusion rules
```

---

## 🛠️ Tech Stack
- **Core**: Python 3.9+
- **Data Science**: Pandas, NumPy, Scikit-Learn
- **Visualization**: Plotly, Seaborn, Matplotlib
- **Web/API**: FastAPI, Uvicorn, Streamlit
- **Deployment Ready**: Joblib for serialization

---

## ⚙️ Installation & Setup

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/your-username/student-performance-prediction.git
   cd student-performance-prediction
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the Model**:
   ```bash
   python src/train.py
   ```

4. **Run the Application**:
   - **Start the UI**: `streamlit run src/dashboard.py`
   - **Start the API**: `python src/api.py`

---

## 🤝 Contribution
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
Developed with ❤️ by Rohan Maurya.
