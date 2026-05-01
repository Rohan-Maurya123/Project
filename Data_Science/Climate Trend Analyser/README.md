# Climate Trend Intelligence

A professional-grade climate data analysis dashboard built with Python, Streamlit, and Plotly. This project demonstrates end-to-end data science capabilities, from synthetic data generation and cleaning to advanced anomaly detection and time-series forecasting.

## Key Features

- **Professional Dark UI**: A sleek, recruiter-ready dashboard with interactive visualizations.
- **Interactive Trend Analysis**: Dynamic rolling mean visualization to track long-term climate changes.
- **Anomaly Detection**: Automated identification of temperature outliers using statistical Z-score analysis.
- **Predictive Forecasting**: 30-day future temperature projections using ARIMA (AutoRegressive Integrated Moving Average) modeling.
- **Dynamic Filters**: Real-time data filtering by date range and anomaly sensitivity.
- **Data Export**: Ability to download processed analysis results as CSV.

## Tech Stack

- **Frontend**: Streamlit
- **Visualization**: Plotly, Matplotlib
- **Data Processing**: Pandas, NumPy
- **Statistics/ML**: Statsmodels (ARIMA)

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd climate-trend-analyser
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Dashboard**:
   ```bash
   streamlit run app.py
   ```

## Project Structure

- `app.py`: Main Streamlit dashboard application.
- `main.py`: CLI entry point for batch analysis.
- `src/`: Core logic modules.
  - `data_simulation.py`: Generates synthetic climate data (2021-2026).
  - `data_loader.py`: Handles data ingestion.
  - `preprocessing.py`: Data cleaning and formatting.
  - `anomaly_detection.py`: Z-score based outlier detection.
  - `trend_analysis.py`: Rolling mean calculations.
  - `forecasting.py`: ARIMA time-series forecasting.
- `data/`: Stores the raw climate dataset.
- `outputs/`: Stores generated plots and CSV analysis results.

## Author

Rohan Maurya
