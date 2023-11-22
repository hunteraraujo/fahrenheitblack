from typing import List, Dict
from pandas import DataFrame
from application.diagnostics import Diagnostics

from data_management.data_retrieval import DataRetrieval
from data_management.data_storage import DataStorage
from order_execution.broker_integration import BrokerIntegration
from order_execution.order_management import OrderManagement
from performance.metrics_calculations import MetricsCalculation
from performance.optimization import Optimization

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
