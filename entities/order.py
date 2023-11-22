class Order:
    def __init__(self, order_type: str, symbol: str, quantity: int, price: float, order_id: str = None):
        self.order_id = order_id
        self.order_type = order_type
        self.symbol = symbol
        self.quantity = quantity
        self.price = price