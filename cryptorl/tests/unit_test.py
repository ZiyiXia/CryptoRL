import numpy as np
import pandas as pd
import yfinance as yf
from cryptorl import tickers, fetch_single, fetch_multiple, get_arrays
from cryptorl import add_indicators, prep_training_data
from cryptorl import get_feature_combinations, cal_avg_rank
from cryptorl import all_lr, dt_pruning, dt_feature_importance, all_nn


def test_tickers():
    assert len(tickers("USD")) > 1


def test_fetch_single_work():
    ret = fetch_single('2022-06-01-00-00', '2022-09-01-00-00', "BTC-USD")
    assert type(ret) == type(pd.DataFrame()), "should return a DataFrame object"


def test_fetch_single_content():
    ret = fetch_single('2022-06-01-00-00', '2022-09-01-00-00', "BTC-USD")
    assert len(ret) == 93, "wrong data amount"


def test_fetch_multiple_work():
    tics = ['BTC-USD', 'ETH-USD']
    ret = fetch_multiple('2022-06-01-00-00', '2022-09-01-00-00', tics)
    assert type(ret) == type(pd.DataFrame()), "should return a DataFrame object"


def test_fetch_multiple_content():
    tics = ['BTC-USD', 'ETH-USD']
    ret = fetch_multiple('2022-06-01-00-00', '2022-09-01-00-00', tics)
    assert len(ret) == 186, "wrong data amount"


def test_add_indicators():
    start = '2023-02-01'
    end = '2023-03-01'
    raw_aapl = yf.download('aapl', start, end)
    processed = add_indicators(raw_aapl)
    assert len(processed.iloc[0]) == 5, "add indicators failed"


def test_prep_training_data():
    comb = ['Price']
    start = '2021-02-01'
    end = '2023-03-01'
    df = yf.download('aapl', start, end)
    processed = add_indicators(df)
    cur_df = processed[comb]
    X, y = prep_training_data(cur_df, 10)
    assert len(X.iloc[0]) == 10 and len(y.iloc[0]) == 1, "prepare training data failed"


# TODO
def test_split():
    pass


def test_get_arrays():
    tics = ['BTC-USD', 'ETH-USD']
    ret = fetch_multiple('2022-06-01-00-00', '2022-09-01-00-00', tics)
    prices = get_arrays(ret)
    assert np.shape(prices) == (2, 93)


def test_get_feature_combinations():
    additional_factors = ['Volume', 'RSI', 'ROC', 'OBV']
    res = get_feature_combinations(additional_factors)
    assert len(res) == 16, "combinations are wrong"


def test_cal_avg_rank():
    test = [[[['a'], 1], [['b'], 2]], [[['a'], 2], [['b'], 1]]]
    res = cal_avg_rank(test)
    assert res[0][0] == 'a', "cal_avg_rank failed"


def test_all_lr():
    additional_factors = ['Volume', 'RSI', 'ROC', 'OBV']
    start = '2021-02-01'
    end = '2023-03-02'
    df = yf.download('aapl', start, end)
    processed_df = add_indicators(df)
    res = all_lr(processed_df, additional_factors)
    assert len(res) == 16, "linear regression failed"


def test_all_nn():
    additional_factors = ['Volume', 'RSI', 'ROC', 'OBV']
    start = '2021-02-01'
    end = '2023-03-02'
    df = yf.download('aapl', start, end)
    processed_df = add_indicators(df)
    res = all_nn(processed_df, additional_factors)
    assert len(res) == 16, "neural network failed"


def test_dt_pruning():
    df = pd.DataFrame()
    res = dt_pruning(df)
    assert len(res) == 0, "decision tree failed"
