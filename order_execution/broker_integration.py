from typing import Dict, List

from ib_insync import IB, Stock, Option, LimitOrder, MarketOrder
from entities.stock_order import StockOrder
from entities.option_order import OptionOrder
from entities.order import Order
from entities.confirmation import Confirmation
from entities.position import Position

class BrokerIntegration:
    """
    BrokerIntegration class to interact with Interactive Brokers using ib_insync.

    This class provides methods to execute orders, query open orders, query current positions,
    and retrieve account details from Interactive Brokers.

    Attributes:
        ib (IB): An instance of the IB class from ib_insync library for broker connection and operations.
    """

    def __init__(self, ib: IB):
        """
        Initializes the BrokerIntegration with a connection to Interactive Brokers.

        Parameters:
            ib (IB): An initialized and connected instance of the IB class.
        """
        self.ib = ib

    def execute_order(self, order: Order) -> Confirmation:
        """
        Executes a trading order using Interactive Brokers.

        The method determines the type of order (stock or option) and creates the appropriate contract.
        It then places the order (market or limit) and checks for its execution status.

        Parameters:
            order (Order): The order to be executed. Can be a StockOrder or OptionOrder.

        Returns:
            Confirmation: An object indicating the status of the order execution.
        """
        # Determine the type of contract based on the order type
        if isinstance(order, StockOrder):
            contract = Stock(order.symbol, 'SMART', 'USD')
        elif isinstance(order, OptionOrder):
            contract = Option(order.symbol, order.expiry, order.strike, order.option_type, 'SMART', 'USD')
        else:
            return Confirmation('ERROR', 'Unsupported order type')

        # Create the appropriate IB order
        if order.order_type == 'MARKET':
            ib_order = MarketOrder('BUY' if order.quantity > 0 else 'SELL', abs(order.quantity))
        elif order.order_type == 'LIMIT':
            ib_order = LimitOrder('BUY' if order.quantity > 0 else 'SELL', abs(order.quantity), order.price)
        else:
            return Confirmation('ERROR', 'Invalid order type')
        
        # Place the order and wait for a status update
        trade = self.ib.placeOrder(contract, ib_order)
        self.ib.waitOnUpdate(timeout=2)

        # Check and return the status of the order
        if trade.orderStatus.status == 'Filled':
            return Confirmation('SUCCESS', 'Order filled')
        elif trade.orderStatus.status in ['Submitted', 'PendingSubmit']:
            return Confirmation('PENDING', 'Order submitted but not filled')
        else:
            return Confirmation('ERROR', 'Order not filled or encountered an error')

    def query_open_orders(self) -> List[Order]:
        """
        Queries and returns a list of open orders.

        Returns:
            List[Order]: A list of open orders currently held in the Interactive Brokers account.
        """
        open_orders = self.ib.openOrders()
        return [self._convert_from_ib_order(order) for order in open_orders]

    def query_positions(self) -> List[Position]:
        """
        Queries and returns a list of current positions.

        Returns:
            List[Position]: A list of current positions held in the Interactive Brokers account.
        """
        positions = self.ib.positions()
        return [Position(pos.contract.symbol, pos.position, pos.avgCost) for pos in positions]

    def query_account_details(self) -> Dict:
        """
        Queries and returns account-related details.

        Returns:
            Dict: A dictionary containing key-value pairs of account details.
        """
        account_values = self.ib.accountValues()
        return {av.tag: av.value for av in account_values}
