import pandas as pd
import numpy as np
from Historic_Crypto import Cryptocurrencies
from Historic_Crypto import HistoricalData


# get valid tickers with given keyword information
def tickers(keyword=None):
    """
    keyword: a string of desired keyword in the ticker id
    """

    df = Cryptocurrencies(coin_search=keyword).find_crypto_pairs()
    tic_list = df.sort_values(by=["id"]).id.to_list()

    return tic_list


# download single ticker's historical price data from Coinbase
def fetch_single(start, end, tic, granularity=86400) -> pd.DataFrame:
    """
    tic: a string of a single ticker
    """

    single_df = HistoricalData(tic, granularity, start, end, verbose=False).retrieve_data()

    return single_df


# download multiple tickers' historical price data from Coinbase
def fetch_multiple(start, end, tickers, granularity=86400) -> pd.DataFrame:
    """
    tickers: a list of the tickers
    start: a string of start time of data
    end: a string of end time of data
    granularity: granularity of the data, choose between 60, 300, 900, 3600, 21600, 86400, default 86400 (1 day)
    """

    whole = pd.DataFrame()
    fail_tics = []

    for tic in tickers:
        temp_df = fetch_single(start, end, tic, granularity)
        temp_df["tic"] = tic
        if len(temp_df) > 0:
            whole = pd.concat([whole, temp_df])
        else:
            fail_tics.append(tic)

    if len(fail_tics) > 0:
        print(fail_tics, "are invalid tickers")

    whole = whole.reset_index().sort_values(by=["time", "tic"]).reset_index(drop=True)

    return whole


# add technical indicators to the current DataFrame
def add_indicators(df) -> pd.DataFrame:
    # TODO
    return df


# split data with given start date and end date
def split(df, start, end) -> pd.DataFrame:
    """
    df: a dataframe object that contains the price data
    start: intentioned start date
    end: intentioned end date
    """
    data = df[(df["date"] >= start) & (df["date"] <= end)]
    data = data.sort_values(["date", "tic"], ignore_index=True)
    data.index = data["date"].factorize()[0]

    return data


# get the prices of tickers in the form of 2d array
def get_arrays(df):
    data = df.copy()
    tickers = data.tic.unique()
    price_arr = []

    for tic in tickers:
        curr_arr = data[data.tic == tic]["close"].values
        price_arr.append(curr_arr)
        # TODO after have indicators, support indicator array

    return np.array(price_arr)


if __name__ == "__main__":
    # tickers = ['BTC-USD', 'ETH-USD']
    # data = fetch_multiple('2020-06-01-00-00', '2020-09-01-00-00', tickers)
    # print(get_arrays(data))

    # print(data[data.tic == 'BTC-USD']["close"].values)

    tics = tickers("USD")[:3]
    ret = fetch_multiple('2022-06-01-00-00', '2022-09-01-00-00', tics)
