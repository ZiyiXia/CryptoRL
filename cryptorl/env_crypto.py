import gym


class CryptoEnv(gym.Env):
    def __init__(self, init_asset) -> None:
        """
        Args:
            init_asset (int): initial amout in the asset

        """
        super().__init__()
        self.capital = init_asset
        self.balance = init_asset
        self.terminal = False
        self.episode = 0

    def reset(self):
        """Rewrite the reset function inherit from gym.Env"""
        pass

    def step(self, action):
        """Rewrite the step function inherit from gym.Env

        Args:
            action (list): an action of buy, hold, or sell
        """
        pass
