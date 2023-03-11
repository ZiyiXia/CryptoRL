import numpy as np
import pandas as pd
from cryptorl import tickers, fetch_single, fetch_multiple, get_arrays


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


# TODO
def test_add_indicators():
    pass


# TODO
def test_split():
    pass


def test_get_arrays():
    tics = ['BTC-USD', 'ETH-USD']
    ret = fetch_multiple('2022-06-01-00-00', '2022-09-01-00-00', tics)
    prices = get_arrays(ret)
    assert np.shape(prices) == (2, 93)
