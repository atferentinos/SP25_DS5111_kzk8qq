from bin.gainers.base import GainerDownload, GainerProcess
import pandas as pd
from datetime import datetime
import time
from pathlib import Path

class GainerDownloadMock(GainerDownload):
    def __init__(self):
        super().__init__(url="mock://test")
        self.csv_file = "mock_gainers.csv"
    
    def download(self):
        print("Using mock data instead of downloading")
        data = {
            "Symbol": ["TEST1", "TEST2", "TEST3"],
            "Name": ["Test Company 1", "Test Company 2", "Test Company 3"],
            "Price": ["100.00", "200.00", "300.00"],
            "Change": ["+5.00", "-2.50", "+1.75"],
            "Change %": ["+5.00%", "-1.25%", "+0.58%"]
        }
        df = pd.DataFrame(data)
        df.to_csv(self.csv_file, index=False)
        print(f"Mock gainers data saved to {self.csv_file}")
        return self.csv_file

class GainerProcessMock(GainerProcess):
    def __init__(self):
        super().__init__()
        self.csv_file = "mock_gainers.csv"
        self.norm_file = "mock_gainers_norm.csv"
    
    def validate_csv_path(self, file_path):
        if not isinstance(file_path, str):
            raise AssertionError(f"Expected string path, got {type(file_path)}")
        path = Path(file_path)
        if not path.exists():
            raise AssertionError(f"File does not exist: {file_path}")
        if path.suffix.lower() != '.csv':
            raise AssertionError(f"File must be a CSV, got: {path.suffix}")
        return path
    
    def transform_stock_data(self, input_df):
        if not isinstance(input_df, pd.DataFrame):
            msg = f"Expected DataFrame, got {type(input_df)}"
            raise AssertionError(msg)
        if input_df.empty:
            raise AssertionError("Input DataFrame is empty")

        required_columns = [
            'symbol',
            'price',
            'price_change',
            'price_percent_change'
        ]

        column_mappings = {
            'Symbol': 'symbol',
            'Price': 'price',
            'Change': 'price_change',
            'Change %': 'price_percent_change'
        }

        output_df = input_df.copy()
        output_df = output_df.rename(columns=column_mappings)
        missing_cols = set(required_columns) - set(output_df.columns)

        if missing_cols:
            msg = f"Missing required columns: {missing_cols}"
            raise AssertionError(msg)

        output_df = output_df[required_columns]

        output_df['source'] = 'Mock Data'
        output_df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if len(output_df.columns) != len(required_columns) + 2:
            raise AssertionError("Output columns don't match required format")
        if output_df.empty:
            raise AssertionError("process resulted in empty df")

        return output_df
    
    def normalize(self):
        print("Normalizing mock gainers data")
        df = pd.read_csv(self.csv_file)
        
        df["Price"] = df["Price"].str.replace("$", "").astype(float)
        df["Change"] = df["Change"].str.replace("+", "").str.replace("-", "-").astype(float)
        df["% Change"] = df["% Change"].str.replace("%", "").str.replace("+", "").astype(float)
        
        df["Source"] = "Mock Data"
        df["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        df.to_csv(self.norm_file, index=False)
        print(f"Normalized mock gainers data saved to {self.norm_file}")
        return self.norm_file
    
    def save_with_timestamp(self):
        print("Saving timestamped mock gainers data")
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_file = f"mock_gainers_norm_{timestamp}.csv"
        
        df = pd.read_csv(self.norm_file)
        df.to_csv(output_file, index=False)
        
        print(f"Saved timestamped file: {output_file}")
        return output_file
