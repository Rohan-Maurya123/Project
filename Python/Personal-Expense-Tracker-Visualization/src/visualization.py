import matplotlib.pyplot as plt

def create_visualizations(df):

    category_spending = df.groupby("Category")["Amount"].sum()

    category_spending.plot(kind="bar")

    plt.title("Category Wise Spending")

    plt.savefig("outputs/charts/category_spending.png")

    monthly = df.groupby(df["Date"].dt.month)["Amount"].sum()

    plt.figure()

    monthly.plot()

    plt.title("Monthly Spending Trend")

    plt.savefig("outputs/charts/monthly_trend.png")