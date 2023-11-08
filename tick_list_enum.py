from enum import Enum, auto
from pandas import DataFrame

class TickListEnum(Enum):
    ADD_CONSTANT = auto()
    MULTIPLY_BY_FACTOR = auto()
    CALCULATE_SMA = auto()

# Associated functions
def add_constant(data: DataFrame, column: str, value: float) -> DataFrame:
    data[column] += value
    return data

def multiply_by_factor(data: DataFrame, column: str, factor: float) -> DataFrame:
    data[column] *= factor
    return data

def calculate_sma(data: DataFrame, column: str, window: int) -> DataFrame:
    """
    Calculates the Simple Moving Average (SMA) for a specified column of a DataFrame.

    Parameters:
        data (DataFrame): The DataFrame containing the data.
        column (str): The name of the column to calculate the SMA for.
        window (int): The number of periods over which to calculate the SMA.
    
    Returns:
        DataFrame: The DataFrame with the SMA values appended as a new column.
    """
    sma_column_name = f"{column}_SMA{window}"
    data[sma_column_name] = data[column].rolling(window=window).mean()
    return data

# Mapping of enum cases to functions
TRANSFORM_FUNCTIONS = {
    TickListEnum.ADD_CONSTANT: add_constant,
    TickListEnum.MULTIPLY_BY_FACTOR: multiply_by_factor,
    TickListEnum.CALCULATE_SMA: calculate_sma
}