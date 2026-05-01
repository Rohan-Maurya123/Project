# 🛡️ Credit Card Fraud Detection

Credit Card Fraud Detection AI is a state-of-the-art Machine Learning application designed to identify and visualize fraudulent credit card transactions in real-time. Featuring a sleek dark-themed dashboard, it provides both single transaction analysis and bulk processing capabilities.

## ✨ Key Features

- **Real-time Prediction**: Instantly analyze transaction risk with a probability gauge.
- **Batch Processing**: Upload CSV files for mass transaction scanning and download results.
- **Interactive Insights**: Explore data patterns through dynamic Plotly charts.
- **Model Transparency**: View top features influencing the AI's decision-making.
- **Modern Dark UI**: A professional, user-friendly interface built with Streamlit.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Credit-Card-Fraud-Detection.git
   cd Credit-Card-Fraud-Detection
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. **Train the model (Optional if .pkl exists)**
   ```bash
   python main.py
   ```

2. **Launch the Dashboard**
   ```bash
   streamlit run app.py
   ```

## 🧠 Model Information

The system utilizes a **Random Forest Classifier** trained on the [Kaggle Credit Card Fraud Detection dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud). To handle the significant class imbalance, **SMOTE** (Synthetic Minority Over-sampling Technique) is applied during the training phase, ensuring high recall for fraudulent cases.

## 📊 Project Structure

- `src/`: Core logic for preprocessing, training, and evaluation.
- `app.py`: Streamlit dashboard implementation.
- `models/`: Stored pre-trained model files.
- `data/`: Dataset storage.
- `outputs/`: Evaluation metrics and plots.

## 🛠️ Built With

- **Streamlit** - Web Dashboard
- **Scikit-Learn** - Machine Learning
- **Plotly** - Interactive Visualizations
- **Pandas/Numpy** - Data Processing
- **Imbalanced-learn** - SMOTE Implementation


