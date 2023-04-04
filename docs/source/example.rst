Examples for the functions
=============================

*tickers()*
------------

The function gets valid tickers with given keyword information. See the following example:

.. code-block:: python

   tickers("USD")

It returns a list containing all the valid tickers with keyword "USD".

*fetch_single()*
-----------------

The function fetches single ticker's historical data from Coinbase. See the following example:

.. code-block:: python

   fetch_single('2020-01-01', '2022-01-01', 'aapl')

It returns a DataFrame object that containing the cleaned data with required ticker and range of dates.

*fetch_multiple()*
-------------------

The function fetches multiple tickers' historical data from Coinbase. See the following example:

.. code-block:: python

   tics = ['BTC-USD', 'ETH-USD']
   fetch_multiple('2020-01-01', '2022-01-01', tics)

It returns a DataFrame object that containing the cleaned data with required ticker and range of dates.

*split()*
-------------------

The function splits the data by given start and end date. See the following example:

.. code-block:: python

   split(df, '2020-01-01', '2022-01-01')

It returns a DataFrame object that in the new range of dates.

*get_arrays()*
-------------------

The function gets the prices of tickers in the form of 2d array. See the following example:

.. code-block:: python

   get_arrays(df)

It returns a list of prices.
