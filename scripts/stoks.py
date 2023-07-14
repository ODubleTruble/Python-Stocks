import yfinance as yf
import pandas as pd


def get_stock_data(ticker: str, start_date: str, end_date: str):
    '''
    Downloads stock data from the ticker from the start_date to end_date.
    Returns the data as a pandas dataframe.
    
    Parameters:
    - ticker: The ticker of the stock.
    - start_date: The start date of the data to return, in the form xxxx-xx-xx, or year-month-day.
    - end_date: The end date.
    '''
    

    data = yf.download(ticker, start_date, end_date)
    data.reset_index(inplace=True)
    
    return data
