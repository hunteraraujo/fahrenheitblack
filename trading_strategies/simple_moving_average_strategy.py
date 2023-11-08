from pandas import DataFrame, Series

from strategy_interface import StrategyInterface

class SimpleMovingAverageStrategy(StrategyInterface):
    """
    A simple moving average crossover strategy implementation.
    """

    def analyze(self, data: DataFrame):
        """
        Analyzes the market data and generates trading signals based on a simple moving average crossover strategy.
        
        Parameters:
            data (DataFrame): The most recent market data to analyze.
        """
        # Assume data contains 'SMA' column with the simple moving average values
        if data['SMA'][-1] > data['SMA'][-2]:
            # Create a Series of 1's with the same index as the data indicating a "buy" signal
            self.signals = Series(1, index=data.index)
        else:
            # Create a Series of -1's with the same index as the data indicating a "sell" signal
            self.signals = Series(-1, index=data.index)