# main.py

from src.config import *
from src.data_loader import *
from src.data_cleaning import *
from src.indicators import *
from src.visualization import *
from src.report_generator import *
from src.backtesting import *
from src.utils import *


def main():

    print("STOCK MARKET DATA ANALYZER")

    create_directories()

    ticker = input("Enter Stock Ticker: ")

    df = fetch_stock_data(
        ticker,
        START_DATE,
        END_DATE
    )

    df = clean_data(df)

    df = calculate_daily_returns(df)

    df = moving_averages(
        df,
        SHORT_MA,
        LONG_MA
    )

    volatility = calculate_volatility(df)

    highest, lowest = highest_lowest_price(df)

    df = simple_moving_average_strategy(df)

    stock_price_chart(df, ticker)

    moving_average_chart(df, ticker)

    return_distribution(df, ticker)

    interactive_candlestick(df, ticker)

    generate_report(
        ticker,
        volatility,
        highest,
        lowest
    )

    df.to_csv(
        f"outputs/csv/{ticker}_analysis.csv",
        index=False
    )

    print("Analysis Completed")


if __name__ == "__main__":
    main()