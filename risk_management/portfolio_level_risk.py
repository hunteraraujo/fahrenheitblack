from main import Portfolio

# TODO: Implement this class
class PortfolioLevelRisk:
    def __init__(self, max_drawdown: float):
        self.max_drawdown = max_drawdown

    def calculate_max_drawdown(self, portfolio: Portfolio) -> float:
        # Code to calculate the maximum drawdown for the portfolio
        pass

    def halt_trading(self, threshold: float):
        # Code to halt trading activities if risk thresholds are breached
        pass