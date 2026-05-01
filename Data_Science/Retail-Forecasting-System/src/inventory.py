import pandas as pd
import numpy as np

def inventory_logic(df):
    """
    Calculates safety stock and reorder point for each product.
    """
    lead_time = 7
    service_level = 1.65  # ~95% service level

    # Calculate rolling std dev per product
    df = df.sort_values(['product_id', 'date'])
    df['std_dev'] = df.groupby('product_id')['sales'].transform(lambda x: x.rolling(window=7, min_periods=1).std()).fillna(0)

    # Safety Stock = Z * std_dev * sqrt(lead_time)
    df['safety_stock'] = service_level * df['std_dev'] * (lead_time ** 0.5)

    # Reorder Point = (Average Daily Sales * Lead Time) + Safety Stock
    # Using forecast as a proxy for average daily sales during lead time
    df['reorder_point'] = df['forecast'] * lead_time + df['safety_stock']

    return df