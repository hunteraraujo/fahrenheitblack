from entities.signal import Signal

class StockSignal(Signal):
    def __init__(self, symbol: str, signal_type: str, quantity: int, order_type: str, price: float):
        super().__init__(symbol, signal_type, quantity, order_type, price)