# TODO: Implement this class
# ? Owner: TradingSystem
# ! TODO: Rework this to be dependent on a dict of strategies and their P/L
from aiohttp_retry import Dict
from entities.portfolio import Portfolio

class Optimization:
    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio

    def apply_half_kelly(self, portfolio: Portfolio) -> Dict:
        # Code to apply the Half Kelly Criterion for portfolio rebalancing
        pass