from typing import Dict, List
from pandas import DataFrame

from entities.order import Order
from entities.trade import Trade

# TODO: Implement this class
class MetricsCalculation:
    def __init__(self):
        self.metrics = None

    def calculate_real_time_metrics(self, data: DataFrame, orders: List[Order]) -> Dict:
        # Code to calculate real-time performance metrics
        pass

    def calculate_post_trade_metrics(self, trades: List[Trade]) -> Dict:
        # Code to calculate post-trade metrics
        pass