import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data(num_products=10, num_days=730):
    """
    Generates a realistic synthetic retail sales dataset.
    """
    np.random.seed(42)
    
    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(num_days)]
    
    products = [f"PRD_{i:03d}" for i in range(1, num_products + 1)]
    categories = ['Electronics', 'Grocery', 'Apparel', 'Home & Kitchen', 'Beauty']
    product_cats = {p: np.random.choice(categories) for p in products}
    product_prices = {p: np.random.uniform(10, 500) for p in products}
    
    data = []
    
    for date in dates:
        is_weekend = date.weekday() >= 5
        month = date.month
        
        for product in products:
            # Base demand
            base_sales = np.random.randint(5, 50)
            
            # Seasonality: higher sales in Dec (Month 12)
            if month == 12:
                base_sales *= 1.5
            
            # Weekend effect
            if is_weekend:
                base_sales *= 1.3
                
            # Random promotion effect (10% chance)
            is_promo = 1 if np.random.random() < 0.1 else 0
            if is_promo:
                base_sales *= 1.8
                
            sales = int(base_sales + np.random.normal(0, 5))
            sales = max(0, sales) # Ensure non-negative
            
            data.append({
                'date': date,
                'product_id': product,
                'category': product_cats[product],
                'price': round(product_prices[product], 2),
                'sales': sales,
                'is_promotion': is_promo,
                'stock_on_hand': np.random.randint(50, 200) # Initial dummy stock
            })
            
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    print("Generating synthetic retail data...")
    df = generate_data()
    df.to_csv("data/sales_data.csv", index=False)
    print(f"Dataset saved to data/sales_data.csv. Shape: {df.shape}")
