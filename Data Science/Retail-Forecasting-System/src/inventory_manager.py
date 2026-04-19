import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime, timedelta

class InventoryManager:
    def __init__(self, model_path="models/sales_forecasting_model.pkl"):
        """
        Initializes the InventoryManager with a trained model.
        """
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
        else:
            self.model = None
        
    def calculate_inventory_metrics(self, avg_daily_sales, std_daily_sales, lead_time=7, service_level=1.65):
        """
        Calculates Safety Stock and Reorder Point.
        service_level: 1.65 for ~95% service level.
        """
        # Safety Stock = Z * std_dev * sqrt(lead_time)
        safety_stock = service_level * std_daily_sales * np.sqrt(lead_time)
        
        # Reorder Point = (Avg Daily Sales * Lead Time) + Safety Stock
        reorder_point = (avg_daily_sales * lead_time) + safety_stock
        
        return {
            'safety_stock': int(np.ceil(safety_stock)),
            'reorder_point': int(np.ceil(reorder_point))
        }

    def get_recommendations(self, df):
        """
        Processes the dataframe and returns inventory recommendations.
        """
        # Ensure column names are lowercase for consistency
        df = df.copy()
        
        # Group by Product to get historical stats
        # We use lowercase 'product_id', 'sales', 'stock_on_hand'
        stats = df.groupby('product_id')['sales'].agg(['mean', 'std']).reset_index()
        
        recommendations = []
        for _, row in stats.iterrows():
            metrics = self.calculate_inventory_metrics(row['mean'], row['std'] if not pd.isna(row['std']) else 0)
            
            # Get latest stock info
            product_df = df[df['product_id'] == row['product_id']]
            current_stock = product_df['stock_on_hand'].iloc[-1]
            
            status = "In Stock"
            if current_stock <= metrics['reorder_point']:
                status = "REORDER NOW"
            elif current_stock <= metrics['reorder_point'] * 1.2:
                status = "Warning: Low Stock"
                
            recommendations.append({
                'Product_ID': row['product_id'],
                'Category': product_df['category'].iloc[0],
                'Avg_Daily_Sales': round(row['mean'], 2),
                'Safety_Stock': metrics['safety_stock'],
                'Reorder_Point': metrics['reorder_point'],
                'Current_Stock': current_stock,
                'Status': status
            })
            
        return pd.DataFrame(recommendations)

if __name__ == "__main__":
    # Test with lowercase data
    if os.path.exists("data/sales_data.csv"):
        df = pd.read_csv("data/sales_data.csv")
        im = InventoryManager()
        recs = im.get_recommendations(df)
        print(recs.head())
    else:
        print("data/sales_data.csv not found. Run main.py first.")
