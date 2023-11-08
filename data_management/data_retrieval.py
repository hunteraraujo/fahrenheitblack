from ib_insync import IB, Stock, Ticker, util
from datetime import datetime
from typing import Callable, List
from pandas import DataFrame

class DataRetrieval:
    """
    A class for retrieving real-time and historical market data using the ib_insync library.
    
    Attributes:
        ib (IB): An instance of the ib_insync.IB class that is already connected to Interactive Brokers.
        callbacks (dict): A dictionary mapping symbols to their corresponding list of callback functions.
    """
    
    def __init__(self, ib: IB):
        """
        The constructor for the DataRetrieval class.
        
        Parameters:
            ib (IB): An instance of the ib_insync.IB class that is already connected to Interactive Brokers.
        """
        self.ib = ib
        self.callbacks = {}  # Maps symbols to lists of callbacks

    # TODO: We should be passing in tickList to filter specific data
    def fetch_realtime_data(self, symbol: str, cb: Callable[[DataFrame], None]) -> None:
        """
        Adds a real-time data handler for a specified symbol.

        Parameters:
            symbol (str): The symbol for which to retrieve real-time data.
            cb (Callable[[DataFrame], None]): The callback function that will handle the real-time data.
        """
        # Define the contract and subscribe to market data
        contract = Stock(symbol, 'SMART', 'USD')
        self.ib.reqMktData(contract)

        # If the symbol isn't in the callbacks dict, add it with an empty list
        if symbol not in self.callbacks:
            self.callbacks[symbol] = []

        # Append the new callback to the list of callbacks for this symbol
        self.callbacks[symbol].append(cb)

        # Attach to the pendingTickersEvent if this is the first symbol being tracked
        if len(self.callbacks) == 1:
            self.ib.pendingTickersEvent += self._on_pending_tickers

    def _on_pending_tickers(self, tickers: List[Ticker]):
        """
        An internal method that is triggered by the pendingTickersEvent. It processes incoming tickers and
        dispatches them to the appropriate callbacks.

        Parameters:
            tickers (List[Ticker]): A list of Ticker objects containing the updated market data.
        """
        for ticker in tickers:
            symbol = ticker.contract.symbol
            if symbol in self.callbacks:
                # Convert ticker to a pandas DataFrame
                df = util.df([ticker])
                # Call all callbacks associated with this symbol with the DataFrame
                for cb in self.callbacks[symbol]:
                    cb(df)

    # TODO: We should be using the tickList to pull down specific historical data
    def fetch_historical_data(self, symbol: str, start_date: datetime, end_date: datetime, frequency: str, tickList: List[str]) -> DataFrame:
        """
        Fetches historical market data for a specified symbol and time frame.

        Parameters:
            symbol (str): The symbol for which to retrieve historical data.
            start_date (datetime): The start date of the historical data query.
            end_date (datetime): The end date of the historical data query.
            frequency (str): The frequency of the historical data (e.g., '1 min', '1 hour').
            tickList (List[str]): A list of specific fields to be included in the returned DataFrame.

        Returns:
            DataFrame: A pandas DataFrame containing the historical market data.
        """
        # Define a contract for the symbol
        contract = Stock(symbol, 'SMART', 'USD')
        # Request historical data for the contract
        bars = self.ib.reqHistoricalData(
            contract,
            endDateTime=end_date.strftime('%Y%m%d %H:%M:%S'),
            durationStr=f'{(end_date - start_date).days} D',
            barSizeSetting=frequency,
            whatToShow='TRADES',
            useRTH=True,
            formatDate=2  # Return as pandas DataFrame
        )
        # Convert the bars to a pandas DataFrame
        df = util.df(bars)
        # If tickList is provided, filter the DataFrame to include only those columns
        if tickList:
            df = df[tickList]
        return df