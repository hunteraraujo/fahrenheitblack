from pandas import Series

# TODO: Implement this class
class StrategyLevelRisk:
    def __init__(self, stop_loss_level: float, take_profit_level: float):
        self.stop_loss_level = stop_loss_level
        self.take_profit_level = take_profit_level

    def apply_stop_loss(self, signals: Series, level: float):
        # Code to apply stop-loss levels to a strategy
        pass

    def apply_take_profit(self, signals: Series, level: float):
        # Code to apply take-profit levels to a strategy
        pass