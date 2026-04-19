from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def forecast_temp(df, steps=30):
    """
    Generates a temperature forecast using ARIMA.
    Returns a dataframe with forecasted dates and values.
    """
    model = ARIMA(df['Temperature'], order=(1, 1, 1))
    model_fit = model.fit()

    forecast_values = model_fit.forecast(steps=steps)
    
    last_date = df['Date'].iloc[-1]
    forecast_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=steps)

    forecast_df = pd.DataFrame({
        'Date': forecast_dates,
        'Forecast': forecast_values
    })
    
    return forecast_df