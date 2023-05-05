import pandas as pd
import numpy as np
import ta
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
    """Add technical indicators to the data (now supporting RSI, ROC, OBV)

    Args:
        df (DataFrame): a df object of raw data

    Returns:
        DataFrame: a df object with added indicators

    """
    ta_rsi = ta.momentum.RSIIndicator(close=df["Adj Close"])
    ta_roc = ta.momentum.ROCIndicator(close=df["Adj Close"])
    ta_obv = ta.volume.OnBalanceVolumeIndicator(close=df["Adj Close"], volume=df["Volume"])
    price_df = df['Adj Close']
    volume_df = df['Volume']
    processed_df = pd.concat([price_df, volume_df], axis=1)
    processed_df["RSI"] = ta_rsi.rsi()
    processed_df["ROC"] = ta_roc.roc()
    processed_df["OBV"] = ta_obv.on_balance_volume()
    processed_df = processed_df.rename({'Adj Close': 'Price'}, axis=1)
    return processed_df


def prep_training_data(df, time_range):
    """Prepare the data for stock prediction

    Args:
        df (DataFrame): a df object of raw data
        time_range: number of dates use as model input

    Returns:
        DataFrame: a df object for model input
        DataFrame: a df object of label

    """
    time_range += 1
    original_columns = df.columns.values.tolist()
    new_columns = []
    label_name = "Price" + str(time_range)
    for day in range(1, time_range):
        for name in original_columns:
            new_columns.append(name + str(day))
    new_columns.append(label_name)

    new_data = []
    for i in range(len(df) - time_range - 1):
        new_row = []
        for day in range(1, time_range):
            for name in original_columns:
                new_row.append(df.iloc[i + day][name])

        new_row.append(df.iloc[i + time_range]["Price"])
        new_data.append(new_row)
    new_df = pd.DataFrame(new_data, columns=[new_columns])
    new_df = new_df.dropna()

    y = new_df[label_name]
    X = new_df.sort_index(axis=1).drop(columns=[label_name])
    return X, y


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
