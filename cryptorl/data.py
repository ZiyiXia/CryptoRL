import pandas as pd
import numpy as np
from Historic_Crypto import Cryptocurrencies
from Historic_Crypto import HistoricalData


def tickers(keyword=None):
    """Get valid tickers with given keyword information

    Args:
        keyword (str): a string of desired keyword in the ticker id

    Returns:
        list: a list of tickers related to the keyword

    """
    df = Cryptocurrencies(coin_search=keyword).find_crypto_pairs()
    tic_list = df.sort_values(by=["id"]).id.to_list()

    return tic_list


def fetch_single(start, end, tic, granularity=86400) -> pd.DataFrame:
    """Fetch single ticker's historical data from Coinbase

    Args:
        start (str): a string of the starting date in the format of year-month-date 'xxxx-xx-xx'
        end (str): a string of the ending date, same format to start
        tic (str): a string of a single ticker

    Returns:
        DataFrame: a df object of the fetched data

    """
    single_df = HistoricalData(tic, granularity, start, end, verbose=False).retrieve_data()

    return single_df


def fetch_multiple(start, end, tickers, granularity=86400) -> pd.DataFrame:
    """Fetch multiple tickers' historical data from Coinbase

    Args:
        start (str): a string of the starting date in the format of year-month-date 'xxxx-xx-xx'
        end (str): a string of the ending date, same format to start
        tickers (list of str): a list of strings of tickers

    Returns:
        DataFrame: a df object of the fetched data

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


def add_indicators(df) -> pd.DataFrame:
    """Add technical indicators to the data

    Args:
        df (DataFrame): a df object of raw data

    Returns:
        DataFrame: a df object with added indicators

    """
    # TODO
    return df


def split(df, start, end) -> pd.DataFrame:
    """Split the data by given start and end date

    Args:
        df (DataFrame): a df object of given data
        start (str): a string of the starting date in the format of year-month-date 'xxxx-xx-xx'
        end (str): a string of the ending date, same format to start

    Returns:
        DataFrame: a df object with expected start and end date

    """
    data = df[(df["date"] >= start) & (df["date"] <= end)]
    data = data.sort_values(["date", "tic"], ignore_index=True)
    data.index = data["date"].factorize()[0]

    return data


def get_arrays(df):
    """Get the prices of tickers in the form of 2d array

    Args:
        df (DataFrame): a df object of given data

    Returns:
        2D NumPy Array: a list of historical price
    """
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
