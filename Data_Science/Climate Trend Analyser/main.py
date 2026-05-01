from src.data_loader import load_data
from src.preprocessing import clean_data
from src.eda import plot_temperature
from src.trend_analysis import trend_analysis
from src.anomaly_detection import detect_anomalies
from src.forecasting import forecast_temp

def main():
    print("🚀 Starting Climate Trend Analysis...")
    
    # 1. Load and Clean Data
    df = load_data("data/climate_data.csv")
    df = clean_data(df)
    print(f"✅ Data loaded: {len(df)} records.")

    # 2. EDA & Visualizations
    plot_temperature(df)
    print("📊 EDA plots generated.")

    # 3. Trend Analysis
    df = trend_analysis(df)
    print("📈 Trend analysis (rolling mean) completed.")

    # 4. Anomaly Detection
    df = detect_anomalies(df)
    anomaly_count = df['Anomaly'].sum()
    print(f"⚠️ Anomaly detection completed: {anomaly_count} anomalies found.")

    # 5. Forecasting
    forecast_df = forecast_temp(df)
    print("🔮 30-day forecast generated.")

    # 6. Save Results
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    
    df.to_csv("outputs/analysis_results.csv", index=False)
    forecast_df.to_csv("outputs/forecast_results.csv", index=False)
    print("💾 All results saved to 'outputs/' directory.")
    print("\n✨ Analysis complete! Run 'streamlit run app.py' to view the dashboard.")

if __name__ == "__main__":
    import os
    main()