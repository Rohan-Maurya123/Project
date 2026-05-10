# src/report_generator.py

def generate_report(ticker, volatility, highest, lowest):

    report = f"""
    ===================================
    STOCK MARKET ANALYSIS REPORT
    ===================================

    Ticker: {ticker}

    Annual Volatility: {volatility:.4f}

    Highest Price: {highest}

    Lowest Price: {lowest}

    Analysis Completed Successfully.
    """

    with open(f"outputs/reports/{ticker}_report.txt", "w") as file:
        file.write(report)

    print(report)