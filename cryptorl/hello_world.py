import pandas as pd
import numpy as np
from Historic_Crypto import HistoricalData
import stable_baselines3
import gym
from stable_baselines3 import A2C
from stable_baselines3 import DDPG
from stable_baselines3 import PPO
from stable_baselines3 import SAC
from stable_baselines3 import TD3


# download historical price data from Coinbase
def fetch_data(ticker, start, end, granularity=86400):
    """
    ticker: the ticker of the coin
    start: start time of data
    end: end time of data
    granularity: granularity of the data, choose between 60, 300, 900, 3600, 21600, 86400, default 86400 (1 day)
    """

    df = HistoricalData(ticker, granularity, start, end).retrieve_data()

    return df


# merge different tickers' dfs together to a single df
def merge_df():
    # TODO
    pass


# make the dataframe to the gym-style environment
def make_env(df):
    # TODO
    pass


# train the DRL agent
def train(model_name, env, steps):
    """
    model_name: chosen DRL algorithm
    env: constructed environment for training DRL agent
    steps: total training steps
    """

    # TODO: support multiple models, e.g. PPO, SAC, etc.

    model = A2C("MlpPolicy", env)
    model = model.learn(total_timesteps=steps)

    return model


# backtest the agent
def trade(model, env):
    # TODO
    pass


if __name__ == "__main__":
    btc = fetch_data('BTC-USD', '2020-06-01-00-00', '2021-06-01-00-00')
    print(btc.head(10))