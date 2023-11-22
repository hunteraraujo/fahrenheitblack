from typing import Dict
from pandas import DataFrame
from trading_strategies.strategy_interface import StrategyInterface

# TODO: Implement this class
# ! Skipping Backtesting Class for MVP (Everything will be backtesting)
class CustomBacktester:
    def __init__(self, strategy: StrategyInterface, data: DataFrame):
        self.strategy = strategy
        self.data = data

    def run_backtest(self, strategy: StrategyInterface, data: DataFrame) -> DataFrame:
        # Code to run backtest for a specific strategy and return results
        pass

    def calculate_performance_metrics(self, results: DataFrame) -> Dict:
        # Code to calculate performance metrics after backtesting
        pass