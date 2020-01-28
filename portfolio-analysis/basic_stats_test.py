'''
This is the test file for basic-stats
Author Nasim
Date 27-01-2020
'''
import pandas as pd
from basic_stats import *
from plotplot import *


def test_get_data():
    symbol = 'AAPL'
    source = 'yahoo'
    start = '01-01-2018'
    end = '01-01-2020'
    adjust_price = False
    return get_data(symbol, source, start, end, adjust_price=False)


def test_plot_stock():
    stock_df = test_get_data()
    symbol = 'AAPL'
    col = 'Adj Close'
    wsize = 30
    price = stock_df[col].values.reshape((-1, 1))
    sma = simple_MA(stock_df[col], window=wsize).values.reshape((-1, 1))
    ewm = simple_ewma(stock_df[col], window=wsize).values.reshape((-1, 1))
    y = np.concatenate((price, sma, ewm), axis=1)
    simple_plot(stock_df.index.values, y,
                title=symbol, xlabel='Date', ylabel="Price",
                legend=['Adj Close', 'MA', 'EMA'])


# def test_plot_bollinger_band():

if __name__ == "__main__":
    test_plot_stock()
    print("Done!")
