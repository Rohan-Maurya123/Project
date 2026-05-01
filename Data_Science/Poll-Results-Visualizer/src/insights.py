def generate_insights(response_counts):
    if response_counts.empty:
        return "No data available to generate insights."
        
    top = response_counts.idxmax()
    total = response_counts.sum()
    top_val = response_counts.max()
    percentage = (top_val / total) * 100
    
    insight = f"**{top}** is the most preferred option, capturing **{percentage:.1f}%** of total responses. "
    
    if len(response_counts) > 1:
        bottom = response_counts.idxmin()
        insight += f"Conversely, **{bottom}** has the lowest preference."
        
    return insight