# 🔮 NEURAL EXPENSE TRACKER - Data Science Project

An advanced, futuristic, AI-styled Expense Tracker application built with Python, Streamlit, and Plotly. This project demonstrates data simulation, cleaning, feature engineering, and high-end interactive visualizations.

## 🚀 Key Features
- **Futuristic AI UI**: A dark-themed, glassmorphic interface with neon accents and pulsing HUD elements.
- **Realistic Data Simulation**: Probabilistic expense generation including weekend spikes and monthly fixed costs.
- **Interactive Analytics**:
    - **Neural Sector Analysis**: Animated stacked bar charts showing monthly spending velocity.
    - **Spending Matrix**: HUD-style donut charts for category breakdowns.
    - **Signal Intensity**: Area and line charts for trend tracking.
- **Neural Insights**: Automated financial advice and overspending detection based on statistical thresholds.
- **Pro DataStream**: A stylized, icon-rich data explorer for raw transaction logs.

## 🛠️ Technology Stack
- **Core**: Python 3.x
- **UI/Dashboard**: [Streamlit](https://streamlit.io/)
- **Data Handling**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Visualizations**: [Plotly Express](https://plotly.com/python/plotly-express/)
- **Animations**: Plotly Animation Frames & CSS3

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/expense-tracker-app.git
   cd expense-tracker-app
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## 🧪 Virtual Simulation Architecture
The system utilizes a **Stochastic Probabilistic Model** to synthesize data:
- **Deterministic Nodes**: Rent and Bills are anchored to the 1st of every month.
- **Weekend Amplification**: A 1.5x multiplier is applied to food and entertainment nodes on weekends.
- **Entropy Logic**: Random probabilities (15% Shopping, 5% Travel) are used to simulate real-world variance.
- **Anomaly Detection**: Uses heuristic-based statistical thresholding to identify overspending events.

## 📂 Project Structure
```text
├── data/               # Raw and cleaned CSV datasets
├── src/                # Core Python logic
│   ├── data_generator.py # Data simulation engine
│   ├── data_cleaning.py  # Preprocessing and feature engineering
│   ├── analysis.py       # Statistical analysis & insights
│   └── visualization.py  # Plotly chart configurations
├── app.py              # Main Streamlit dashboard
├── main.py             # CLI pipeline execution script
└── requirements.txt    # Project dependencies
```

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
