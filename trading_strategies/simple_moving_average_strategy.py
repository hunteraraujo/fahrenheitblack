from entities.stock_signal import StockSignal
from trading_strategies.strategy_interface import StrategyInterface
from pandas import DataFrame

class SimpleMovingAverageStrategy(StrategyInterface):
    """
    A simple moving average crossover strategy implementation.
    
    This strategy generates buy or sell signals based on the crossover of the simple 
    moving average. A buy signal is generated when the current SMA value crosses above 
    the previous SMA value, and a sell signal when it crosses below.
    """

    def analyze(self, data: DataFrame):
        """
        Analyzes the market data and generates trading signals based on a simple moving 
        average crossover strategy.
        
        Parameters:
            data (DataFrame): The most recent market data to analyze. It is assumed 
            that the DataFrame contains a 'Close' column for closing prices and an 'SMA' 
            column for simple moving average values.
        """
        self.signals = []

        # Example parameters for signal generation
        symbol = "AAPL"  # Example stock symbol
        quantity = 100  # Example quantity
        order_type = "MARKET"  # or "LIMIT"
        price = data['Close'][-1]  # Current closing price, for example

        # Signal generation logic
        if data['SMA'][-1] > data['SMA'][-2]:
            signal_type = "BUY"
            signal = StockSignal(symbol, signal_type, quantity, order_type, price)
            self.signals.append(signal)
        else:
            signal_type = "SELL"
            signal = StockSignal(symbol, signal_type, quantity, order_type, price)
            self.signals.append(signal)
