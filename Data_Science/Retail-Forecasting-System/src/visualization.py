import matplotlib.pyplot as plt
import os

def plot_sales(df, product_id=None):
    """
    Plots actual sales vs forecasted sales.
    If product_id is None, it plots aggregate sales.
    """
    os.makedirs("outputs", exist_ok=True)
    
    plt.figure(figsize=(12, 6))
    
    if product_id:
        plot_df = df[df['product_id'] == product_id]
        title = f"Sales Forecast for {product_id}"
    else:
        # Aggregate across all products by date
        plot_df = df.groupby('date')[['sales', 'forecast']].sum().reset_index()
        title = "Aggregate Sales Forecast"

    plt.plot(plot_df['date'], plot_df['sales'], label="Actual Sales", color='blue', alpha=0.7)
    plt.plot(plot_df['date'], plot_df['forecast'], label="Forecasted Sales", color='red', linestyle='--')
    
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Sales Units")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("outputs/forecast_plot.png")
    plt.close() # Close to free memory
    print(f"Plot saved to outputs/forecast_plot.png")