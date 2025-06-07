#install yfinance library : pip install yfinance
import yfinance as yf
def get_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data for a given ticker symbol between specified dates.
    
    :param ticker: Stock ticker symbol (e.g., 'AAPL' for Apple Inc.)
    :param start_date: Start date in 'YYYY-MM-DD' format
    :param end_date: End date in 'YYYY-MM-DD' format
    :return: DataFrame containing historical stock data
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data
def main():
    ticker = input("Enter the stock ticker symbol (e.g., AAPL): ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    try:
        stock_data = get_stock_data(ticker, start_date, end_date)
        print(stock_data)
    except Exception as e:
        print(f"An error occurred: {e}")
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