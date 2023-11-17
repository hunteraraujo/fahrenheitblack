class Order:
    def __init__(self, order_id: str, order_type: str, symbol: str, quantity: int, price: float):
        self.order_id = order_id
        self.order_type = order_type
        self.symbol = symbol
        self.quantity = quantity
        self.price = price