import gym


class CryptoEnv(gym.Env):
    def __init__(self, init_asset) -> None:
        super().__init__()
        self.capital = init_asset
        self.balance = init_asset
        self.terminal = False
        self.episode = 0

    def reset(self):
        pass

    def step(self, action):
        pass
