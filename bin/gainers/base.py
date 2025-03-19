from abc import ABC, abstractmethod
import pandas as pd
from pathlib import Path

class GainerDownload(ABC):
    """Base class for downloading stock gainer data."""
    
    def __init__(self, url):
        """Initialize with the URL to scrape."""
        self.url = url
        self.html_file = None
        self.csv_file = None
    
    @abstractmethod
    def download(self):
        """
        Download data from the source URL and save to CSV.
        
        Returns:
            str: Path to the CSV file if successful, None otherwise.
        """
        pass

class GainerProcess(ABC):
    """Base class for processing stock gainer data."""
    
    def __init__(self, source_name):
        """Initialize with the source name."""
        self.source_name = source_name
        self.csv_file = None
        self.norm_file = None
    
    @abstractmethod
    def validate_csv_path(self, file_path):
        """
        Validate that the CSV file exists and is valid.
        
        Args:
            file_path (str): Path to the CSV file.
            
        Returns:
            Path: Validated Path object.
            
        Raises:
            AssertionError: If validation fails.
        """
        pass
    
    @abstractmethod
    def transform_stock_data(self, input_df):
        """
        Transform the stock data into a standardized format.
        
        Args:
            input_df (pd.DataFrame): Input DataFrame.
            
        Returns:
            pd.DataFrame: Transformed DataFrame.
            
        Raises:
            AssertionError: If transformation fails.
        """
        pass
    
    @abstractmethod
    def normalize(self):
        """
        Normalize the CSV data.
        
        Returns:
            str: Path to the normalized CSV file if successful, None otherwise.
        """
        pass
    
    @abstractmethod
    def save_with_timestamp(self):
        """
        Save the normalized data with a timestamp.
        
        Returns:
            str: Path to the timestamped CSV file if successful, None otherwise.
        """
        pass
