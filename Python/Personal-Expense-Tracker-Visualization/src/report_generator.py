def generate_report(df):

    report = df.groupby("Category")["Amount"].sum()

    report.to_csv("outputs/reports/category_report.csv")

    print("Report Generated")