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


def get_symbols(paramdict={'Test Issue': [0],
                           'Financial Status': ['N']}):
    '''
    get the list of symbols from
    :param paramdict: a dictionary of all possible inputs that can passed to
    get_nasdaq_symbols
    ETF :0,1
    Market Category: [' ', 'G', 'Q', 'S']
    Listing Exchange: [N,P,Q,A,Z,V]
    Test Issue = 0,1
    Financial Status:[NaN, N, D, H, E]
    More info can be found in
    http://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs

    :return: a dataframe
    '''
    df = pdr.get_nasdaq_symbols()
    for k in paramdict.keys():
        df = df[df[k].isin(paramdict[k])]

    return df


def get_symbol_info(symbols, info):
    '''
    getting a list of symbols and return a dataframe corresponding to list of info
    :param symbols: a list of market traded
    :param info: a list of information that can be provided by yahoo
    :return: a dataframe: index are symbols and info is the column
    '''
    return pdr.get_quote_yahoo(symbols)[info]


def choose_instrumets(filename, ni=100, sort_col=None, **kwargs):
    '''

    :param filename: the csv file name for specific attribute
    :param ni: number of stocks to return
    :param sort:
    :return: a dataframe of all instruments for analysis
    '''

    df = pd.read_csv(filename, index_col=0)
    if sort_col:
        df = df.sort_values(by=[sort_col], **kwargs)

    return df.ix[:ni]

def simple_ma(df, window=15, func='mean'):
    if func == 'mean':
        return df.rolling(window=window).mean()
    elif func == 'std':
        return df.rolling(window=window).std(ddof=0)  # Population
    else:
        print("the func parameter not recognized.")
        return -1


def simple_ewma(df, window=15, func='mean'):
    if func == 'mean':
        return df.ewm(span=window, adjust=False).mean()
    elif func == 'std':
        return df.ewm(span=window, adjust=False).std(ddof=0)  # population
    else:
        print("the func parameter not recognized.")
        return -1


def bollinger_band(df, window=20, method="SMA"):
    if method == "SMA":
        mean = simple_ma(df, window=window, func='mean')
        ssd = simple_ma(df, window=window, func='std')
    elif method == "EMA":
        mean = simple_ewma(df, window=window, func='mean')
        ssd = simple_ewma(df, window=window, func='std')
    else:
        print("the method function is not recognized.")
    upper = mean + 2 * ssd
    lower = mean - 2 * ssd

    return mean, upper, lower


if __name__ == "__main__":
    print("hello world")
