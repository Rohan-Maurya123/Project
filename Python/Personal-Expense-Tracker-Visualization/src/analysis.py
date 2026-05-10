def run_analysis(df):

    print("\nTotal Spending:")
    print(df["Amount"].sum())

    print("\nHighest Spending Category:")
    print(df.groupby("Category")["Amount"].sum().idxmax())

    print("\nAverage Daily Spending:")
    print(df.groupby("Date")["Amount"].sum().mean())