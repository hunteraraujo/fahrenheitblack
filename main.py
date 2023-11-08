from typing import List, Dict
from pandas import DataFrame

from data_management.data_retrieval import DataRetrieval
from data_management.data_storage import DataStorage

from trading_strategies.strategy_interface import StrategyInterface

from entities.activity import Activity
from entities.alert import Alert
from entities.confirmation import Confirmation
from entities.order import Order
from entities.portfolio import Portfolio
from entities.position import Position
from entities.signal import Signal
from entities.status import Status
from entities.trade import Trade
from entities.update import Update

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
