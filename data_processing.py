from pandas import DataFrame
from typing import List, Tuple

from tick_list_enum import TRANSFORM_FUNCTIONS, TickListEnum

class DataProcessing:
    """
    A class for processing data by applying a series of transformations defined by a list of operations.
    
    Attributes:
        data (DataFrame): The data to be transformed.
    """
    
    def __init__(self, data: DataFrame):
        """
        The constructor for DataProcessing class.
        
        Parameters:
            data (DataFrame): The initial DataFrame to be processed.
        """
        self.data = data

    def transform_data(self, data: DataFrame, expr: List[Tuple[TickListEnum, List]]) -> DataFrame:
        """
        Transforms the DataFrame based on a list of expressions representing different operations.
        
        Parameters:
            data (DataFrame): The DataFrame to be transformed.
            expr (List[Tuple[TickListEnum, List]]): A list of tuples, where each tuple contains an enum value 
                                                     representing the operation to be performed, and a list of 
                                                     parameters for the callable function associated with that operation.
        
        Returns:
            DataFrame: The transformed DataFrame.
        """
        for operation, params in expr:
            if operation in TRANSFORM_FUNCTIONS:
                # Retrieve the function associated with the enum value
                function = TRANSFORM_FUNCTIONS[operation]
                # Call the function with the provided parameters
                data = function(data, *params)
            else:
                raise ValueError(f"Operation {operation} is not supported.")
        return data