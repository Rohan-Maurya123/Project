# 🏠 House Price Prediction App (INR)

An interactive Machine Learning web application built with Streamlit to predict house prices. The app converts predictions to Indian Rupees (INR) and provides insightful data visualizations.

## 🚀 Features

- **Price Prediction**: Estimate house prices in Lakhs and Crores.
- **Interactive UI**: User-friendly sliders and inputs for house features.
- **Data Analytics**: Interactive charts using Plotly (Histograms, Scatter plots, Heatmaps).
- **Modern Design**: Clean interface with custom CSS and animations.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Machine Learning**: Scikit-Learn (Random Forest Regressor)
- **Data Visualization**: Plotly, Seaborn, Matplotlib
- **Language**: Python 3.x

## 📁 Project Structure

```text
├── app/
│   └── streamlit_app.py    # Streamlit application UI
├── data/
│   └── housing.csv         # Dataset
├── models/
│   └── model.pkl           # Trained Random Forest model
├── src/
│   ├── load_data.py        # Data loading utility
│   ├── preprocess.py       # Data preprocessing logic
│   ├── train_model.py      # Model training script
│   ├── evaluate.py         # Model evaluation script
│   └── predict.py          # Prediction helper
├── main.py                 # Main pipeline script
└── requirements.txt        # Project dependencies
```

## ⚙️ Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd "House Price Prediction"
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model** (Optional):
   ```bash
   python main.py
   ```

4. **Run the app**:
   ```bash
   streamlit run app/streamlit_app.py
   ```

## 📊 Dataset

The project uses the Boston Housing Dataset, which includes features like crime rate, number of rooms, and tax rates to predict the median value of homes.

---
Developed with ❤️ by Rohan Maurya.
