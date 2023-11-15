from entities.order import Order

class StockOrder(Order):
    def __init__(self, order_type: str, symbol: str, quantity: int, price: float):
        super().__init__(order_type, symbol, quantity, price)