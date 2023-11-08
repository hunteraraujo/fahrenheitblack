from entities import Position
from typing import List

class Portfolio:
    def __init__(self, positions: List[Position], initial_balance: float, current_balance: float):
        self.positions = positions
        self.initial_cash = initial_balance
        self.current_cash = current_balance