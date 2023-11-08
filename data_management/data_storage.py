import pandas as pd
from pandas import DataFrame

class DataStorage:
    """
    A class for handling the storage and retrieval of data in CSV format.
    
    Attributes:
        data_path (str): The file path where CSV files will be saved and loaded from.
    """
    
    def __init__(self, data_path: str):
        """
        The constructor for the DataStorage class.
        
        Parameters:
            data_path (str): The base directory to save and load CSV files.
        """
        self.data_path = data_path
    
    def save_to_csv(self, data: DataFrame, filename: str) -> None:
        """
        Saves a pandas DataFrame to a CSV file at the specified filename.
        
        Parameters:
            data (DataFrame): The DataFrame to be saved to CSV.
            filename (str): The filename for the CSV file. If the filename does not end in '.csv',
                            it will be appended automatically.
        """
        # Ensure the filename ends with .csv
        if not filename.endswith('.csv'):
            filename += '.csv'
        full_path = f"{self.data_path}/{filename}"
        # Save the DataFrame to a CSV file
        data.to_csv(full_path, index=False)
        # Index is set to False to avoid writing row numbers
    
    def load_from_csv(self, filename: str) -> DataFrame:
        """
        Loads a pandas DataFrame from a CSV file with the specified filename.
        
        Parameters:
            filename (str): The filename of the CSV file to be loaded. If the filename does not end
                            in '.csv', it will be appended automatically.
        
        Returns:
            DataFrame: The DataFrame that is loaded from the CSV file.
        """
        # Ensure the filename ends with .csv
        if not filename.endswith('.csv'):
            filename += '.csv'
        full_path = f"{self.data_path}/{filename}"
        # Load the DataFrame from a CSV file
        return pd.read_csv(full_path)
