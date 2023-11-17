from entities.order import Order

class OptionOrder(Order):
    def __init__(self, order_id: str, order_type: str, symbol: str, quantity: int, price: float, strike: float, expiry: str, option_type: str):
        super().__init__(order_id, order_type, symbol, quantity, price)
        self.strike = strike
        self.expiry = expiry  # Format: YYYYMMDD
        self.option_type = option_type  # 'C' for Call, 'P' for Put
