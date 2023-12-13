from typing import List
from application.diagnostics import Diagnostics

from data_management.data_retrieval import DataRetrieval
from data_management.data_storage import DataStorage
from order_execution.broker_integration import BrokerIntegration
from order_execution.order_management import OrderManagement
from performance.metrics_calculations import MetricsCalculation
from performance.optimization import Optimization

from trading_strategies.strategy_interface import StrategyInterface
from trading_strategies.simple_moving_average_strategy import SimpleMovingAverageStrategy

from entities.order import Order

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
        self.broker_integration = BrokerIntegration()
        self.portfolio = self.broker_integration.query_account_details()
        self.optimization = Optimization(self.portfolio)
        self.diagnostics = Diagnostics([])

    def run(self):
        # Code to run the trading system

        # ? This is where we would have the main loop that runs the trading system

        print("🚀 🤑 $ 💲 ＄ 💵 💰 Running trading system.")

        pass

broker_integration = BrokerIntegration()
order_manager = OrderManagement(broker_integration=broker_integration)
strategy1 = StrategyExecutor(
    strategy=SimpleMovingAverageStrategy(),
    order_manager=order_manager,
    metrics_calculations=MetricsCalculation(),
    data_retrieval=DataRetrieval(),
)
trading_system = TradingSystem([strategy1])
trading_system.run()