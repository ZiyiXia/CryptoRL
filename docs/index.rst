.. CryptoRL documentation master file, created by
   sphinx-quickstart on Sat Apr  1 20:44:05 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CryptoRL's documentation!
====================================

CryptoRL is a library that provides a full pipeline of fetchng data, cleaning data, constructing environment, and training models for crypto historical data.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Installation
-------------

To install CryptoRL, simply run:

.. code-block:: bash

   pip install cryptorl

Usage
-------

After successfully installed CryptoRL, you can import by:

.. code-block:: python

   import data from cryptorl

and download data by:

.. code-block:: python

   df = data.fetch_single('2020-01-01', '2022-01-01', 'aapl')

Autodocs
----------

.. toctree::
   :maxdepth: 2

   source/example
   source/cryptorl
   source/modules