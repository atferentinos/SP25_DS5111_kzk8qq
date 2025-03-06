from bin.gainers.base import GainerDownload, GainerProcess
import pandas as pd
from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup
import time
from pathlib import Path

class YahooGainerDownload(GainerDownload):
    def __init__(self):
        super().__init__(url="https://finance.yahoo.com/gainers")
        self.html_file = "ygainers.html"
        self.csv_file = "ygainers.csv"
    
    def download(self):
        print("Downloading yahoo gainers")
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            print(f"Requesting URL: {self.url}")
            response = requests.get(self.url, headers=headers, timeout=30)
            print(f"Response status code: {response.status_code}")
            
            if response.status_code != 200:
                print(f"Error: Received non-200 status code: {response.status_code}")
                return None
            
            with open(self.html_file, "w", encoding="utf-8") as f:
                f.write(response.text)
            
            print(f"HTML content saved to {self.html_file} (size: {len(response.text)} bytes)")
            
            # Try parsing with pandas read_html which is more robust
            try:
                print("Attempting to parse HTML with pandas...")
                dfs = pd.read_html(self.html_file)
                
                if dfs and len(dfs) > 0:
                    print(f"Found {len(dfs)} tables with pandas")
                    # Use the first table that looks like a gainers table
                    for i, df in enumerate(dfs):
                        print(f"Table {i} has {len(df)} rows and columns: {list(df.columns)}")
                        if len(df) >= 5 and len(df.columns) >= 5:
                            print(f"Using table {i}")
                            df.to_csv(self.csv_file, index=False)
                            print(f"Data saved to {self.csv_file}")
                            return self.csv_file
                
                print("No suitable tables found with pandas, falling back to BeautifulSoup")
            except Exception as e:
                print(f"Pandas parsing failed: {str(e)}, falling back to BeautifulSoup")
            
            # Fall back to BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Try multiple possible selectors
            table = None
            selectors = [
                "table.W(100%)",  # Old selector
                "div[data-test='fin-screener'] table",  # Possible new selector
                "section[data-test='screener-results'] table",  # Another possibility
                "div.Ovx(a) table",  # General table in overflow area
                "#scr-res-table"  # Table ID sometimes used
            ]

            for selector in selectors:
                try:
                    print(f"Trying selector: {selector}")
                    elements = soup.select(selector)
                    if elements:
                        table = elements[0]
                        print(f"Found table with selector: {selector}")
                        break
                except Exception as e:
                    print(f"Error with selector {selector}: {str(e)}")

            if not table:
                # If still not found, try a more general approach
                tables = soup.find_all('table')
                print(f"Found {len(tables)} tables on the page")
                if tables:
                    # Use the first table with enough rows
                    for i, t in enumerate(tables):
                        rows = t.find_all('tr')
                        print(f"Table {i} has {len(rows)} rows")
                        if len(rows) > 5:  # Assuming gainers table has at least 5 rows
                            table = t
                            print(f"Using table {i} with {len(rows)} rows")
                            break
            
            if not table:
                print("Error: Could not find table in HTML")
                print("Page title:", soup.title.text if soup.title else "No title")
                print("First 500 chars of HTML:", response.text[:500])
                
                # Last resort: try Chrome headless
                print("Trying Chrome headless as last resort...")
                import subprocess
                try:
                    result = subprocess.run([
                        "sudo", "google-chrome-stable", "--headless", "--disable-gpu", 
                        "--dump-dom", "--no-sandbox", "--timeout=5000", 
                        "https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200"
                    ], capture_output=True, text=True, timeout=60)
                    
                    if result.returncode != 0:
                        print(f"Chrome error: {result.stderr}")
                        return None
                        
                    with open(self.html_file, "w", encoding="utf-8") as f:
                        f.write(result.stdout)
                    
                    # Try parsing with pandas again
                    dfs = pd.read_html(self.html_file)
                    if dfs and len(dfs) > 0:
                        dfs[0].to_csv(self.csv_file, index=False)
                        print(f"Data saved to {self.csv_file} using Chrome")
                        return self.csv_file
                    else:
                        print("No tables found with Chrome approach")
                        return None
                except Exception as e:
                    print(f"Chrome approach failed: {str(e)}")
                    return None
                
                return None
            
            data = []
            
            rows = table.find_all('tr')
            print(f"Found {len(rows)} rows in table")
            
            for row in rows[1:]:  # Skip header row
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 5:
                    symbol = cols[0].text.strip()
                    name = cols[1].text.strip()
                    price = cols[2].text.strip()
                    change = cols[3].text.strip()
                    percent_change = cols[4].text.strip()
                    
                    data.append({
                        "Symbol": symbol,
                        "Name": name,
                        "Price": price,
                        "Change": change,
                        "Change %": percent_change
                    })
            
            print(f"Extracted {len(data)} gainers from table")
            
            if not data:
                print("Warning: No data extracted from table")
                return None
                
            df = pd.DataFrame(data)
            
            df.to_csv(self.csv_file, index=False)
            print(f"Data saved to {self.csv_file}")
            return self.csv_file
        except Exception as e:
            print(f"Error in download method: {str(e)}")
            import traceback
            traceback.print_exc()
            return None

class YahooGainerProcess(GainerProcess):
    def __init__(self):
        super().__init__(source_name="yahoo")
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
        try:
            # Check if file exists
            if not os.path.exists(self.csv_file):
                print(f"Error: CSV file not found: {self.csv_file}")
                return None
                
            # Load the data
            df = pd.read_csv(self.csv_file)
            print(f"Loaded CSV with {len(df)} rows")
            
            if df.empty:
                print("Error: Empty dataframe loaded from CSV")
                return None
                
            print(f"Columns in CSV: {', '.join(df.columns)}")
            
            # Handle the case where Price column has complex formats
            if "Price" in df.columns:
                print("Sample Price values:", df["Price"].head().tolist())
                # Extract just the first number (current price)
                df["Price"] = df["Price"].astype(str).str.extract(r'(\d+\.?\d*)').astype(float)
            
            # Similar handling for change columns
            if "Change" in df.columns:
                print("Sample Change values:", df["Change"].head().tolist())
                # Extract the number with sign
                df["Change"] = df["Change"].astype(str).str.extract(r'([+-]?\d+\.?\d*)').astype(float)
                
            if "Change %" in df.columns:
                print("Sample Change % values:", df["Change %"].head().tolist())
                # Extract percentage number
                df["Change %"] = df["Change %"].astype(str).str.extract(r'([+-]?\d+\.?\d*)').astype(float)
            
            df["Source"] = "Yahoo Finance"
            df["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Save normalized data
            df.to_csv(self.norm_file, index=False)
            print(f"Normalized data saved to {self.norm_file}")
            return self.norm_file
            
        except Exception as e:
            print(f"Error in normalize method: {str(e)}")
            import traceback
            traceback.print_exc()
            return None
    
    def save_with_timestamp(self):
        print("Saving Yahoo gainers with timestamp")
        try:
            # Check if file exists
            if not os.path.exists(self.norm_file):
                print(f"Error: Normalized CSV file not found: {self.norm_file}")
                return None
            
            # Create data directory if it doesn't exist
            os.makedirs("data", exist_ok=True)
            
            # Generate timestamped filename
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_file = f"data/ygainers_norm_{timestamp}.csv"
            
            # Load and save data
            df = pd.read_csv(self.norm_file)
            
            if df.empty:
                print("Error: Empty dataframe loaded from normalized CSV")
                return None
                
            df.to_csv(output_file, index=False)
            
            print(f"Saved timestamped file: {output_file}")
            return output_file
            
        except Exception as e:
            print(f"Error in save_with_timestamp method: {str(e)}")
            import traceback
            traceback.print_exc()
            return None
