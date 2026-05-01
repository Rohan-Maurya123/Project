# 📊 Poll Results Visualizer

A professional, interactive dashboard for visualizing and analyzing poll results. This project transforms raw survey data into actionable insights through a modern Streamlit interface.

## 🚀 Features

- **Interactive Dashboard**: Modern tabbed interface for Overview, Segment Analysis, and Raw Data.
- **Dynamic Filtering**: Filter data by Region and Age Group in real-time.
- **Interactive Charts**: High-quality, interactive visualizations using Altair (with tooltips and zoom).
- **KPI Metrics**: Instant snapshot of key performance indicators like Total Responses and Top Preferences.
- **Automated Insights**: Smart text-based summaries of the data trends.
- **Data Export**: Download filtered datasets directly from the dashboard.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Data Analysis**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Visualization**: [Altair](https://altair-viz.github.io/)
- **Language**: Python 3.x

## 📁 Project Structure

```text
Poll-Results-Visualizer/
├── app/
│   └── app.py              # Main Streamlit application
├── data/
│   └── poll_data.csv       # Generated dataset (git-ignored)
├── src/
│   ├── analysis.py         # Data processing logic
│   ├── data_generator.py   # Script to generate dummy data
│   ├── data_loader.py      # Data loading utilities
│   ├── insights.py         # Automated insight generation
│   ├── preprocessing.py    # Data cleaning logic
│   └── visualization.py    # Interactive chart definitions
├── main.py                 # Data generation entry point
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## ⚙️ Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Poll-Results-Visualizer.git
   cd Poll-Results-Visualizer
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate the initial dataset**:
   ```bash
   python main.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app/app.py
   ```

## 📊 Usage

- Use the **Sidebar** to filter the results by Region or Age Group.
- Explore the **Overview** tab for a high-level summary and response distribution.
- Check the **Segment Analysis** tab for deeper dives into regional and demographic trends.
- Use the **Data View** tab to inspect the raw records or download the filtered data.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
