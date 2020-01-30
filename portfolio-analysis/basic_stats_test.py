'''
This is the test file for basic-stats
Author Nasim
Date 27-01-2020
'''
import pandas as pd
from basic_stats import *
from plotplot import *


def test_get_data(symbol):
    source = 'yahoo'
    start = '01-01-2018'
    end = '01-01-2020'
    adjust_price = False
    return get_data(symbol, source, start, end, adjust_price=False)


def test_plot_stock():
    symbol = 'AAPL'
    col = 'Adj Close'
    wsize = 30

    stock_df = test_get_data(symbol)
    price = stock_df[col].values.reshape((-1, 1))
    sma = simple_ma(stock_df[col], window=wsize).values.reshape((-1, 1))
    ewm = simple_ewma(stock_df[col], window=wsize).values.reshape((-1, 1))
    y = np.concatenate((price, sma, ewm), axis=1)
    simple_plot(stock_df.index.values, y,
                title=symbol, xlabel='Date', ylabel="Price",
                legend=['Adj Close', 'MA', 'EMA'])


def test_bollinger_band(plot=False):
    symbol = 'IBM'
    col = 'Adj Close'
    wsize = 20
    method = 'SMA'
    stock_df = test_get_data(symbol)
    mean, upper_band, lower_band = bollinger_band(stock_df[col], wsize,
                                                  method=method)
    mean = mean.values.reshape((-1, 1))
    upper_band = upper_band.values.reshape((-1, 1))
    lower_band = lower_band.values.reshape((-1, 1))

    if plot:
        price = stock_df[col].values.reshape((-1, 1))
        y = np.concatenate((price, mean, upper_band, lower_band), axis=1)
        simple_plot(stock_df.index.values, y,
                    title=('Bollinger Band for ' + symbol),
                    xlabel='Date',
                    ylabel="Price",
                    legend=['Adj Close', 'mean', 'upper', 'lower'])


def test_get_symbols():
    df = get_symbols(paramdict={'Test Issue': [0],
                                'Financial Status': ['N'],
                                'ETF': [0]})
    print(df.info())


def test_get_symbol_info():
    df = get_symbols(paramdict={'Test Issue': [0],
                                'Financial Status': ['N'],
                                'ETF': [1]})

    sym_list = df['NASDAQ Symbol'].values
    return get_symbol_info(sym_list, 'marketCap')


def generate_marketcap_file():
    suffx = ['G', 'Q', 'S', 'ETF']
    dt = '20200129'
    prfx = 'MarketCap'

    out_df = pd.DataFrame(columns=["MarketCap", 'Market Category'])
    for s in suffx:
        df = pd.read_csv(prfx + '_' + dt + '_' + s + '.csv', index_col=0)
        df.columns = ['MarketCap']
        df['Market Category'] = s
        out_df = pd.concat([out_df, df])
    out_df.to_csv(prfx + '_' + dt + '.csv')
    return out_df


def test_choose_instrumets():
    filename = 'MarketCap_20200129.csv'
    return choose_instrumets(filename, ni=100, sort_col='MarketCap',
                                ascending=False, na_position='last')


if __name__ == "__main__":
    df= test_choose_instrumets()
    print(df.shape)
    print("Done!")
