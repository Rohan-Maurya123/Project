import pandas as pd

def analyze_data(file_path="data/cleaned_expenses.csv"):
    """
    Performs in-depth analysis and generates key metrics.
    """
    try:
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

    # Filter for Expenses only for spending analysis
    expenses_df = df[df['Type'] == 'Expense']
    income_df = df[df['Type'] == 'Income']

    # 1. High-level Metrics
    total_expenses = expenses_df['Amount'].sum()
    total_income = income_df['Amount'].sum()
    net_savings = total_income - total_expenses
    avg_daily_spending = total_expenses / df['Date'].nunique()

    # 2. Category Analysis
    category_sum = expenses_df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    top_category = category_sum.index[0] if not category_sum.empty else "N/A"

    # 3. Monthly Trends
    monthly_trend = expenses_df.groupby("Year_Month")["Amount"].sum()

    # 4. Weekend vs Weekday
    weekend_avg = expenses_df[expenses_df['Is_Weekend']]['Amount'].mean()
    weekday_avg = expenses_df[~expenses_df['Is_Weekend']]['Amount'].mean()

    # 5. Overspending Detection (Threshold: > 1.5x average daily)
    daily_spending = expenses_df.groupby("Date")["Amount"].sum()
    threshold = daily_spending.mean() * 1.5
    overspending_days = daily_spending[daily_spending > threshold]

    metrics = {
        "total_expenses": total_expenses,
        "total_income": total_income,
        "net_savings": net_savings,
        "avg_daily_spending": avg_daily_spending,
        "top_category": top_category,
        "category_sum": category_sum,
        "monthly_trend": monthly_trend,
        "weekend_avg": weekend_avg,
        "weekday_avg": weekday_avg,
        "overspending_days": len(overspending_days)
    }

    print("Analysis Complete")
    return metrics

def generate_insights(metrics):
    """
    Generates automated insights based on metrics.
    """
    insights = []
    
    # Savings Insight
    savings_rate = (metrics['net_savings'] / metrics['total_income']) * 100
    if savings_rate > 20:
        insights.append(f"Great job! Your savings rate is {savings_rate:.1f}%.")
    else:
        insights.append(f"Your savings rate is {savings_rate:.1f}%. Try to keep it above 20%.")

    # Category Insight
    insights.append(f"Your highest spending is in {metrics['top_category']}.")

    # Weekend Insight
    if metrics['weekend_avg'] > metrics['weekday_avg'] * 1.2:
        ratio = (metrics['weekend_avg'] / metrics['weekday_avg'])
        insights.append(f"Weekend spending is {ratio:.1f}x higher than weekdays. Plan your leisure activities better!")

    # Overspending Insight
    if metrics['overspending_days'] > 5:
        insights.append(f"You had {metrics['overspending_days']} days of high overspending this period.")

    return insights

if __name__ == "__main__":
    m = analyze_data()
    if m:
        print(generate_insights(m))