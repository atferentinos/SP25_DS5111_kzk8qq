from bin.gainers.base import GainerDownload, GainerProcess
import pandas as pd
from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup
import time
from pathlib import Path

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        super().__init__(url="https://finance.yahoo.com/gainers")
        self.html_file = "ygainers.html"
        self.csv_file = "ygainers.csv"
    
    def download(self):
        print("Downloading yahoo gainers")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/58.0.3029.110"
        }
        response = requests.get(self.url, headers=headers)
        
        with open(self.html_file, "w", encoding="utf-8") as f:
            f.write(response.text)
        
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", {"class": "W(100%)"})
        
        data = []
        
        rows = table.find_all("tr")
        for row in rows[1:]:
            cols = row.find_all("td")
            if len(cols) >= 5:
                symbol = cols[0].text
                name = cols[1].text
                price = cols[2].text
                change = cols[3].text
                percent_change = cols[4].text
                
                data.append({
                    "Symbol": symbol,
                    "Name": name,
                    "Price": price,
                    "Change": change,
                    "Change %": percent_change
                })
        
        df = pd.DataFrame(data)
        
        df.to_csv(self.csv_file, index=False)
        return self.csv_file

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        super().__init__()
        self.csv_file = "ygainers.csv"
        self.norm_file = "ygainers_norm.csv"
    
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

        output_df['source'] = 'Yahoo Finance'
        output_df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if len(output_df.columns) != len(required_columns) + 2:
            raise AssertionError("Output columns don't match required format")
        if output_df.empty:
            raise AssertionError("process resulted in empty df")

        return output_df
    
    def normalize(self):
        print("Normalizing yahoo gainers")
        df = pd.read_csv(self.csv_file)
        
        df["Price"] = df["Price"].str.replace("$", "").astype(float)
        
        df["Change"] = df["Change"].str.replace("+", "").str.replace("-", "-").astype(float)
        df["% Change"] = df["% Change"].str.replace("%", "").str.replace("+", "").astype(float)
        
        df["Source"] = "Yahoo Finance"
        
        df["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        df.to_csv(self.norm_file, index=False)
        return self.norm_file
    
    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_file = f"ygainers_norm_{timestamp}.csv"
        
        df = pd.read_csv(self.norm_file)
        
        df.to_csv(output_file, index=False)
        
        print(f"Saved timestamped file: {output_file}")
        return output_file
