import pandas as pd
from cryptorl import tickers, fetch_multiple, get_arrays


def test_fetching_process():
    tics = tickers("USD")[20:22]
    ret = fetch_multiple('2022-06-01-00-00', '2022-09-01-00-00', tics)
    assert type(ret) == type(pd.DataFrame()), "should return a DataFrame object"
    prices = get_arrays(ret)
    assert len(prices) > 0, "prices are empty"
