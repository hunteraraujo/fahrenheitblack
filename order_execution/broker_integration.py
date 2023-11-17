from typing import Dict, List

from ib_insync import IB, Stock, Option, LimitOrder, MarketOrder, Contract
from ib_insync.order import Order as IBOrder
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

    def cancel_order(self, order: Order) -> Confirmation:
        """
        Cancels a trading order using Interactive Brokers.

        Parameters:
            order (Order): The order to be cancelled.

        Returns:
            Confirmation: An object indicating the status of the order cancellation.
        """
        self.ib.cancelOrder(order.orderId)
        return Confirmation('SUCCESS', 'Order cancelled')

    def modify_order(self, old_order: Order, new_order: Order) -> Confirmation:
        """
        Modifies a trading order using Interactive Brokers.

        Parameters:
            old_order (Order): The order to be modified.
            new_order (Order): The new order parameters.

        Returns:
            Confirmation: An object indicating the status of the order modification.
        """
        self.cancel_order(old_order)
        return self.execute_order(new_order)
    
    def _convert_from_ib_order(self, ib_order: IBOrder) -> Order:
        """
        Converts an ib_insync order to a custom Order object.

        Parameters:
            ib_order (ib_insync.Order): The ib_insync order to be converted.

        Returns:
            Order: The converted custom Order object.
        """

        trade = next((trade for trade in self.ib.trades() if trade.order.orderId == ib_order.orderId), None)
        if trade is None:
            raise ValueError(f"No trade found with orderId: {ib_order.orderId}")
        contract = trade.contract

        if contract.secType == 'STK':
            return StockOrder(
                order_id=ib_order.orderId,
                order_type=ib_order.orderType,
                symbol=contract.symbol,
                quantity=ib_order.totalQuantity,
                price=ib_order.lmtPrice if ib_order.orderType == 'LMT' else ib_order.auxPrice
            )
        elif contract.secType == 'OPT':
            return OptionOrder(
                order_id=ib_order.orderId,
                order_type=ib_order.orderType,
                symbol=contract.symbol,
                quantity=ib_order.totalQuantity,
                price=ib_order.lmtPrice if ib_order.orderType == 'LMT' else ib_order.auxPrice,
                strike=contract.strike,
                expiry=contract.lastTradeDateOrContractMonth,
                option_type=contract.right
            )
        else:
            raise ValueError(f"Unsupported secType: {contract.secType}")
        
    # def _convert_from_ib_order(self, ib_order) -> Order:
    #     """
    #     Converts an Interactive Brokers order object to a local Order object (StockOrder or OptionOrder).

    #     Parameters:
    #         ib_order: The order object from Interactive Brokers.

    #     Returns:
    #         Order: The corresponding local Order object.
    #     """
    #     # Extract common order attributes
    #     order_id = ib_order.orderId
    #     order_type = 'MARKET' if isinstance(ib_order, MarketOrder) else 'LIMIT'
    #     quantity = ib_order.totalQuantity
    #     price = ib_order.lmtPrice if order_type == 'LIMIT' else None

    #     # Retrieve the contract using the referenceContractId
    #     contract = self.ib.qualifyContracts(Contract(conId=ib_order.order.conId))[0]

    #     # Check the type of contract and create the appropriate order object
    #     if contract.secType == 'STK':
    #         symbol = contract.symbol
    #         return StockOrder(order_id, order_type, symbol, quantity, price)
    #     elif contract.secType == 'OPT':
    #         symbol = contract.symbol
    #         strike = contract.strike
    #         expiry = contract.lastTradeDateOrContractMonth
    #         option_type = contract.right
    #         return OptionOrder(order_id, order_type, symbol, quantity, price, strike, expiry, option_type)
    #     else:
    #         # Handling for unsupported contract types, if necessary
    #         pass