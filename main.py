#install yfinance library : pip install yfinance
import yfinance as yf
import difflib
import pandas as pd #pip install lxml
from datetime import datetime


"""We need to make sure that the user actually types in a valid symbol (S & P 500 Only for now)"""
def get_sp500_tickers():
    # Fetch S&P 500 tickers from Wikipedia
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pd.read_html(url)
    sp500_df = tables[0]
    return sp500_df['Symbol'].tolist()

"""If the user enters an incorrect ticker symbol suggest one that is close to the one they entered"""
def suggest_ticker(user_input, valid_tickers):
    return difflib.get_close_matches(user_input.upper(), valid_tickers, n=3, cutoff=0.5)

"""User will always be prompted to enter a valid ticker symbol"""
def get_validated_ticker(valid_tickers):
    while True:
        user_input = input("Enter an S&P 500 stock ticker (e.g., AAPL): ").upper()
        if user_input in valid_tickers:
            return user_input
        else:
            print("Invalid ticker symbol.")
            suggestions = suggest_ticker(user_input, valid_tickers)
            if suggestions:
                print("Did you mean one of these?")
                for s in suggestions:
                    print(f" - {s}") 

"""Observe Stock Data"""
def get_stock_data(ticker, start_date, end_date):
    return yf.download(ticker, start=start_date, end=end_date)

"""Ensure valid Date & Time is entered"""
def get_valid_date(start, end):
    while True:
        date_str = input(start)
        date_str2 = input(end)
        try:
            # Try to parse the date
            datetime.strptime(date_str, "%Y-%m-%d")
            datetime.strptime(date_str2, "%Y-%m-%d")
            return date_str, date_str2
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


"""Combine"""
def main():
    print("Extracting S&P 500")
    valid_tickers = get_sp500_tickers()

    # Obtain ticker symbol (AAPL, AMZN, NFLX, etc.)
    ticker = get_validated_ticker(valid_tickers)

    # Obtain start and end dates in year, month, day
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Validate the date inputs
    get_valid_date(start_date, end_date)

    # Fetch and display stock data (Dataframe)
    try:
        data = get_stock_data(ticker, start_date, end_date)
        if data.empty:
            print("No data available for the given range.")
        else:
            print(f"\nHistorical data for {ticker}:\n")
            print(data)
    except Exception as e:
        print(f"Something went wrong: {e}")

# Initalize
if __name__ == "__main__":
    main()

# This script fetches historical stock data for a given ticker symbol between specified dates.
# It uses the yfinance library to download the data and prints it to the console.
# Ensure you have the yfinance library installed before running this script.
# Example usage:
# python main.py
# Enter the stock ticker symbol (e.g., AAPL): AAPL
# Enter the start date (YYYY-MM-DD): 2023-01-01
# Enter the end date (YYYY-MM-DD): 2023-12-31
# The script will output the historical stock data for Apple Inc. between the specified dates.
# Note: The script assumes that the user inputs valid ticker symbols and date formats.
# The yfinance library allows for easy access to financial data from Yahoo Finance.
# Make sure to handle exceptions for invalid inputs or network issues.
# The script is designed to be run from the command line and will prompt the user for input.
# You can modify the ticker symbol and date range as needed to fetch data for different stocks.
# The output will be a DataFrame containing the stock's historical prices, volumes, and other relevant data.