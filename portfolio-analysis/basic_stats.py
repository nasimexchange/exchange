import numpy as np
import pandas as pd
import pandas_datareader as pdr


def get_data(symbol, source, start_date, end_date, adjust_price=False):
    '''
    this function is simply scrap the data from any given source
    which is readable  by pandas-reader

    Parameters
    ----------
    symbol: a symbol to retrieve data
    source: can be any recognized source like yahoo, google
    start_date : string, int, date, datetime, Timestamp
        Starting date. Parses many different kind of date
        representations (e.g., 'JAN-01-2010', '1/1/10', 'Jan, 1, 1980'). Defaults to
        5 years before current date.
    end_date : string, int, date, datetime, Timestamp
        Ending date
    adjust_price : bool, default False
        If True, adjusts all prices in hist_data ('Open', 'High', 'Low',
        'Close') based on 'Adj Close' price. Adds 'Adj_Ratio' column and drops
        'Adj Close'.
    return: a data frame with datetime index
    '''
    if source.lower() == 'yahoo':
        return pdr.get_data_yahoo(symbol, start=start_date, end=end_date)
    else:
        return pdr.data.DataReader(symbol, data_source=source,
                                   start=start_date,
                                   end=end_date)

def simple_MA(df, window=15, func='mean'):
    if func=='mean':
        return df.rolling(window=window).mean()
    elif func == 'std':
        return df.rolling(window=window).std()
    else:
        print("the func parameter not recognized.")
        return -1


def simple_ewma(df, window=15, func='mean'):
    if func=='mean':
        return df.ewm(span=window, adjust=False).mean()
    elif func == 'std':
        return df.ewm(span=window, adjust=False).std()
    else:
        print("the func parameter not recognized.")
        return -1






if __name__ == "__main__":
    print("hello world")
