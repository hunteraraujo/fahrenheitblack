from typing import Dict
from entities.confirmation import Confirmation
from entities.option_order import OptionOrder
from entities.option_signal import OptionSignal
from entities.order import Order
from entities.signal import Signal
from entities.status import Status
from entities.stock_order import StockOrder
from entities.stock_signal import StockSignal
from order_execution.broker_integration import BrokerIntegration

class OrderManagement:
    """
    A class to manage the order lifecycle in a trading system. This class handles
    creating, monitoring, canceling, and modifying orders through a broker integration.

    Attributes:
        broker_integration (BrokerIntegration): An instance of BrokerIntegration that handles
                                                communication with the broker.

    Methods:
        create_order(signal: Signal) -> Order: Creates an order based on the provided signal.
        monitor_order(order: Order) -> Status: Checks the current status of the given order.
        cancel_order(order: Order) -> Confirmation: Cancels the specified order.
        modify_order(old_order: Order, new_order: Order) -> Confirmation: Modifies an existing order.
    """

    def __init__(self, broker_integration: BrokerIntegration):
        """
        Initializes the OrderManagement class with the provided broker integration.

        Args:
            broker_integration (BrokerIntegration): An instance of BrokerIntegration to be used
                                                    for order management.
        """
        self.broker_integration = broker_integration

    def create_order(self, signal: Signal) -> Order:
        """
        Creates an Order object based on the type and details of the provided signal.

        Args:
            signal (Signal): A Signal object containing the details for the order creation.
                             This could be a StockSignal or an OptionSignal.

        Returns:
            Order: An instance of Order (StockOrder or OptionOrder) based on the signal type.

        Raises:
            ValueError: If the signal type is unsupported.
        """
        if isinstance(signal, StockSignal):
            return StockOrder(
                order_type=signal.order_type,
                symbol=signal.symbol,
                quantity=signal.quantity,
                price=signal.price
            )
        elif isinstance(signal, OptionSignal):
            return OptionOrder(
                order_type=signal.order_type,
                symbol=signal.symbol,
                quantity=signal.quantity,
                price=signal.price,
                strike=signal.strike,
                expiry=signal.expiry,
                option_type=signal.option_type
            )
        else:
            raise ValueError("Unsupported signal type")

    def monitor_order(self, order: Order) -> Status:
        """
        Queries the current status of the given order using the broker integration.

        Args:
            order (Order): The Order object whose status needs to be monitored.

        Returns:
            Status: The current status of the order.
        """
        return self.broker_integration.query_order_status(order)

    def cancel_order(self, order: Order) -> Confirmation:
        """
        Requests cancellation of the specified order using the broker integration.

        Args:
            order (Order): The Order object to be canceled.

        Returns:
            Confirmation: A Confirmation object indicating the outcome of the cancel request.
        """
        return self.broker_integration.cancel_order(order)

    def modify_order(self, old_order: Order, new_order: Order) -> Confirmation:
        """
        Requests modification of an existing order with new parameters.

        Args:
            old_order (Order): The original Order object to be modified.
            new_order (Order): The new Order object with updated order details.

        Returns:
            Confirmation: A Confirmation object indicating the outcome of the modify request.
        """
        return self.broker_integration.modify_order(old_order, new_order)