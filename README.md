# CryptoRL
Fetching time series data of cryptocurrencies and using ML and RL to do cryptocurrency trading.

[![License: MIT](https://img.shields.io/github/license/ZiyiXia/CryptoRL)](https://opensource.org/licenses/MIT)

[![GitHub Issue](https://img.shields.io/github/issues/ZiyiXia/CryptoRL)](https://github.com/ZiyiXia/CryptoRL/issues)

[![PyPI](https://img.shields.io/pypi/v/CryptoRL)](https://pypi.org/project/CryptoRL/)

![](https://img.shields.io/github/actions/workflow/status/ZiyiXia/CryptoRL/build.yml?label=build%20status&logo=github)

[![codecov](https://img.shields.io/codecov/c/github/ZiyiXia/CryptoRL?logo=codecov)](https://app.codecov.io/gh/ZiyiXia/CryptoRL)

[![docs](https://img.shields.io/readthedocs/cryptorl)](https://cryptorl.readthedocs.io)


## Overview
CryptoRL will use popular deep reinforcement learning algorithms and machine learning algorithms to do cryptocurrency trading.

## Installation

Run ```pip install cryptorl``` to install CryptoRL.

## Getting started

To fetch data, please use the functions in *data.py*.

For example:

```fetch_single('2020-01-01', '2022-01-01', 'aapl')```

will return a DataFrame object that containing the cleaned data with required ticker and range of dates.

With well processed data, you can use *env_crypto.py* to construct crypto market environment.

Read the [documentation](https://cryptorl.readthedocs.io) for more details.
