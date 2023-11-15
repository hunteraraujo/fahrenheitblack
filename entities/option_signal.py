from entities.signal import Signal


class OptionSignal(Signal):
    def __init__(self, symbol: str, signal_type: str, quantity: int, order_type: str, price: float, strike: float, expiry: str, option_type: str):
        super().__init__(symbol, signal_type, quantity, order_type, price)
        self.strike = strike
        self.expiry = expiry
        self.option_type = option_type