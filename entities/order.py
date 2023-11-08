class Order:
    def __init__(self, order_type: str, symbol: str, quantity: int, price: float):
        self.order_type = order_type
        self.symbol = symbol
        self.quantity = quantity
        self.price = price