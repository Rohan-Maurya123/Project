# Employee Performance Predictor 🚀

An end-to-end Machine Learning application designed to predict employee performance levels (High, Medium, Low) using historical data analytics and professional metrics. This project demonstrates a complete data science lifecycle from synthetic data generation to a web-based deployment.

## 📊 Project Overview

This tool helps HR departments and managers identify high-potential employees and those needing support by analyzing key performance indicators (KPIs) such as experience, training hours, feedback scores, and project delivery.

## 🛠️ Tech Stack

- **Language:** Python 3.13
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (Random Forest Classifier)
- **Visualization:** Matplotlib, Seaborn
- **Web App:** Streamlit
- **Model Serialization:** Joblib

## 🏗️ Project Structure

```text
├── app/
│   └── app.py              # Streamlit Web Application
├── data/
│   └── dataset.csv         # Generated Employee Dataset
├── models/
│   └── model.pkl           # Trained RF Model & Encoders
├── src/
│   ├── data_generator.py   # Synthetic data generation logic
│   ├── preprocessing.py    # Data cleaning & feature engineering
│   ├── model.py            # Model training & hyperparameter tuning
│   ├── evaluate.py         # Performance metrics & feature importance
│   └── eda.py              # Exploratory Data Analysis scripts
├── main.py                 # Project execution pipeline
└── requirements.txt        # Project dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Employee-Performance-Predictor
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate # Linux/Mac
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 📈 How to Run

1. **Run the full pipeline (Data -> Preprocessing -> Training -> Evaluation):**
   ```bash
   python main.py
   ```

2. **Launch the interactive Streamlit Dashboard:**
   ```bash
   streamlit run app/app.py
   ```

## 🧠 Model Performance

The project uses a **Random Forest Classifier** optimized via `GridSearchCV`. 
- **Key Features:** Feedback Score, Experience, Projects Handled, Training Hours.
- **Accuracy:** ~90%+ (on synthetic data).

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
Developed by [Your Name]
