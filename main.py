from datetime import datetime
from typing import List, Dict
from pandas import DataFrame, Series


class Order:
    def __init__(self, order_type: str, symbol: str, quantity: int, price: float):
        self.order_type = order_type
        self.symbol = symbol
        self.quantity = quantity
        self.price = price


class Position:
    def __init__(self, symbol: str, quantity: int, price: float):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price


class Signal:
    def __init__(self, symbol: str, signal_type: str, price: float):
        self.symbol = symbol
        self.signal_type = signal_type
        self.price = price


class Trade:
    def __init__(self, symbol: str, quantity: int, price: float):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price


class Portfolio:
    def __init__(self, positions: List[Position], initial_balance: float, current_balance: float):
        self.positions = positions
        self.initial_cash = initial_balance
        self.current_cash = current_balance


class Update:
    def __init__(self, update_type: str, description: str):
        self.update_type = update_type
        self.description = description


class Alert:
    def __init__(self, alert_type: str, message: str):
        self.alert_type = alert_type
        self.message = message


class Activity:
    def __init__(self, activity_type: str, description: str):
        self.activity_type = activity_type
        self.description = description


class Confirmation:
    def __init__(self, confirmation_type: str, message: str):
        self.confirmation_type = confirmation_type
        self.message = message


class Status:
    def __init__(self, status_type: str, message: str):
        self.status_type = status_type
        self.message = message


class DataRetrieval:
    def __init__(self, provider: str, symbol: str):
        self.provider = provider  # The data provider to be used for fetching data. e.g. NASDAQ, Yahoo Finance, etc.
        self.symbol = symbol  # The trading symbol for which data is to be retrieved.

    # ! TODO: This will probably change, will need to be a callback for an event from the ib_insync library
    def fetch_realtime_data(self, symbol: str, cb: callable) -> Series:
        # Code to fetch real-time data for the specified symbol
        # Passes the data to the callback function
        # Returns the data as a Series
        pass

    def fetch_historical_data(
        self,
        symbol: str,
        start_date: datetime,
        end_date: datetime,
        frequency: str,
        tickList: List[str],
    ) -> DataFrame:
        # Code to fetch historical data for a specified time frame
        pass


class DataStorage:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def save_to_csv(self, data: DataFrame, filename: str):
        # Code to save data to a CSV file
        pass

    def load_from_csv(self, filename: str) -> DataFrame:
        # Code to load data from a CSV file
        pass


class DataProcessing:
    def __init__(self, data: DataFrame):
        self.data = data

    def clean_data(self, data: DataFrame) -> DataFrame:
        # Code to clean and preprocess data
        pass

    # ? Leaving vague for now, this *may* be more for transforming necessary data in some
    # ? way separate from clean_data (e.g. calculating a volume-weighted average price)
    # ? Rather than just cleaning/preprocessing the data

    # ? What we may do is keep the strategy data processing example below specific to the
    # ? StrategyInterface.analyze method.
    def transform_data(self, data: DataFrame, expr: List[str]) -> DataFrame:
        # Code to apply necessary transformations or calculations

        # ! Hot take: "expr" would be replaced with a list of tickList items (from an enum)
        # ! Just adding columns to the DataFrame with the tickList calculations

        pass

    # ? Example: This is an example that may not be what it actually do be.
    # ! This would NOT be a subclass, but keeping the functions separate would be good :+1:
    # class MyStrategyDataProcessing (DataProcessing):
    #     def __init__(self, data: DataFrame):
    #         super().__init__(data)

    #     def clean_data(self, data: DataFrame) -> DataFrame:
    #         # Code to clean and preprocess data
    #         pass

    #     def get_sma(self, data: DataFrame, window: int) -> DataFrame:
    #         # Code to calculate the simple moving average
    #         pass

    #     def transform_data(self, data: DataFrame, expr: str) -> DataFrame:
    #         # Code to apply necessary transformations or calculations

    #         # Example: Calculate the 50-day simple moving average
    #         data['SMA'] = self.get_sma(data, 50)

    #         pass


# ! Skipping Risk Management for MVP
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

# ! Skipping Risk Management for MVP
class PortfolioLevelRisk:
    def __init__(self, max_drawdown: float):
        self.max_drawdown = max_drawdown

    def calculate_max_drawdown(self, portfolio: Portfolio) -> float:
        # Code to calculate the maximum drawdown for the portfolio
        pass

    def halt_trading(self, threshold: float):
        # Code to halt trading activities if risk thresholds are breached
        pass

class StrategyInterface:
    def __init__(
            self,
            data: DataFrame,
        ):
        self.data = data
        self.signals = None

    def analyze(self, data: DataFrame) -> Series:
        # Code to analyze data and generate trading signals

        # Sets self.signals to a Series of trading signals

        # Pass in the most recent data since the last time analyze was called
        # ! The strategy itself would be in this function

        # e.g.:
        # if data['SMA'][-1] > data['SMA'][-2]:)
        #     self.signals = Series(1, index=data.index)
        # else:
        #     self.signals = Series(-1, index=data.index)

        pass


class OrderManagement:
    def __init__(self):
        self.orders = None

    def create_order(self, signal: Signal) -> Order:
        # Code to create a new order based on trading signal
        pass

    def monitor_order(self, order: Order) -> Status:
        # Code to monitor the status of an open order
        pass

    def cancel_order(self, order: Order) -> Confirmation:
        # Code to cancel an open order
        pass

    def modify_order(self, order: Order, modifications: Dict) -> Confirmation:
        # Code to modify an existing order
        pass


class MetricsCalculation:
    def __init__(self):
        self.metrics = None

    def calculate_real_time_metrics(self, data: DataFrame, orders: List[Order]) -> Dict:
        # Code to calculate real-time performance metrics
        pass

    def calculate_post_trade_metrics(self, trades: List[Trade]) -> Dict:
        # Code to calculate post-trade metrics
        pass


class StrategyExecutor:
    def __init__(
        self,
        strategy: StrategyInterface,
        order_manager: OrderManagement,
        metrics_calculations: MetricsCalculation,
        data_retrieval: DataRetrieval,
    ):
        self.strategy = strategy
        self.order_manager = order_manager
        self.metrics_calculations = metrics_calculations
        self.data_retrieval = data_retrieval

    def execute(self, orders: List[Order]):
        # Code to execute trading signals and generate orders   
        self.data_retrieval.fetch_realtime_data(
            "AAPL",
            self.strategy.analyze(self.strategy.data)
        )

        pass

    def scale_strategy(self, factor: float):
        # Code to scale a strategy based on performance
        pass

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


class PerformanceAnalysis:
    def __init__(self, results: DataFrame):
        self.results = results

    def visualize_results(self, results: DataFrame):
        # Code to generate visualizations for backtesting results
        pass

# ? Owner: TradingSystem
class BrokerIntegration:
    def __init__(self, broker: str):
        self.broker = broker

    def execute_order(self, order: Order) -> Confirmation:
        # Code to execute order and return confirmation
        pass

    def query_open_orders(self) -> List[Order]:
        # Code to return a list of open orders
        pass

    def query_positions(self) -> List[Position]:
        # Code to return a list of current positions
        pass

    def query_account_details(self) -> Dict:
        # Code to return account-related details
        pass

# ? Owner: TradingSystem
# ! TODO: Rework this to be dependent on a dict of strategies and their P/L
class Optimization:
    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio

    def apply_half_kelly(self, portfolio: Portfolio) -> Dict:
        # Code to apply the Half Kelly Criterion for portfolio rebalancing
        pass

# ! Skipping for MVP
class UpdatesManagement:
    def __init__(self, updates: List[Update]):
        self.updates = updates

    def apply_update(self, update: Update) -> Confirmation:
        # Code to apply system updates or bug fixes
        pass

# ? Owner: TradingSystem
class Diagnostics:
    def __init__(self, alerts: List[Alert]):
        self.alerts = alerts

    def send_alert(self, alert: Alert) -> Confirmation:
        # Code to send real-time alerts via SMS or email
        pass

    def log_activity(self, activity: Activity):
        # Code to log system activities and performance
        pass


class TradingSystem:
    def __init__(self, executors: List[StrategyExecutor]):
        self.executors = executors
        # Used to store positions, orders, etc. in case of app failure
        self.data_storage = DataStorage("data/")
        self.broker_integration = BrokerIntegration("IBKR")
        self.portfolio = self.broker_integration.query_account_details()
        self.optimization = Optimization(self.portfolio)
        self.diagnostics = Diagnostics([])

    def run(self):
        # Code to run the trading system

        # ? This is where we would have the main loop that runs the trading system

        pass





    # ! Everything below this line was before we started working on the TradingSystem class
    # data_retrieval = DataRetrieval("NASDAQ", "AAPL")

    # # Fetch real-time data
    # data = data_retrieval.fetch_realtime_data("AAPL")
    # self.data_storage.save_to_csv(data, "AAPL.csv")

    # # Connect to the broker
    # broker_integration = BrokerIntegration("IBKR")

    # # Fetch historical data
    # data = data_retrieval.fetch_historical_data(
    #     "AAPL",
    #     datetime(2020, 1, 1),
    #     datetime(2020, 12, 31),
    #     "1d",
    #     ["open", "high", "low", "close", "volume"],
    # )
    # self.data_storage.save_to_csv(data, "AAPL.csv")

    # # Load data from CSV
    # data = self.data_storage.load_from_csv("AAPL.csv")

    # # Clean and preprocess data
    # data_processing = DataProcessing(data)
    # data = data_processing.clean_data(data)

    # # Apply transformations
    # data = data_processing.transform_data(data, ["SMA"])

    # # Create strategy
    # class MyStrategy(StrategyInterface):
    #     def __init__(self, data: DataFrame):
    #         super().__init__(data)

    #     def analyze(self, data: DataFrame) -> Series:
    #         if data["SMA"][-1] > data["SMA"][-2]:
    #             self.signals = Series(1, index=data.index)
    #         else:
    #             self.signals = Series(-1, index=data.index)

    #         return self.signals

    # strategy = MyStrategy(data)

    # # Create another strategy
    # class MyStrategy2(StrategyInterface):
    #     def __init__(self, data: DataFrame):
    #         super().__init__(data)

    #     def analyze(self, data: DataFrame) -> Series:
    #         if data["SMA"][-1] > data["SMA"][-2]:
    #             self.signals = Series(1, index=data.index)
    #         else:
    #             self.signals = Series(-1, index=data.index)

    #         return self.signals

    # strategy2 = MyStrategy2(data)

    # # Execute strategy
    # order_management = OrderManagement()
    # strategy_executor = StrategyExecutor(strategy)

    # orders = strategy_executor.execute(strategy.signals)

    # order_management.create_order(orders)

    # pass
