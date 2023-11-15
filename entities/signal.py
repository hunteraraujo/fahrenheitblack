class Signal:
    def __init__(self, symbol: str, signal_type: str, quantity: int, order_type: str, price: float):
        self.symbol = symbol
        self.signal_type = signal_type  # e.g., 'BUY', 'SELL'
        self.quantity = quantity
        self.order_type = order_type  # 'MARKET' or 'LIMIT'
        self.price = price  # Relevant for limit orders