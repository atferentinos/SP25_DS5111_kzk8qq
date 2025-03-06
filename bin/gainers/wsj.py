from bin.gainers.base import GainerDownload, GainerProcess
import pandas as pd
from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup
import time
from pathlib import Path

class WSJGainerDownload(GainerDownload):
    def __init__(self):
        super().__init__(url="https://www.wsj.com/market-data/stocks/marketsdiary")
        self.html_file = "wsjgainers.html"
        self.csv_file = "wsjgainers.csv"
    
    def download(self):
        print("Downloading WSJ gainers")
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
            
            # Try multiple possible selectors for WSJ Markets Diary tables
            table = None
            selectors = [
                "table.WSJTables--table",  # Common WSJ table class
                ".wsj-table-gainers table",  # Possible gainers table
                "table.gainers-table",  # Another possible class
                "#market-data-gainers table",  # Market data gainers
                "div.module div.table-container table",  # General table in module
                "table"  # Last resort - any table
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
                return None
            
            data = []
            
            rows = table.find_all('tr')
            print(f"Found {len(rows)} rows in table")
            
            # Try to find headers first to map columns correctly
            header_row = rows[0] if rows else None
            headers = []
            if header_row:
                headers = [th.text.strip() for th in header_row.find_all(['th', 'td'])]
                print(f"Found headers: {headers}")
            
            # Determine column indices based on headers or use defaults
            symbol_idx = next((i for i, h in enumerate(headers) if 'symbol' in h.lower() or 'ticker' in h.lower()), 0)
            name_idx = next((i for i, h in enumerate(headers) if 'name' in h.lower() or 'company' in h.lower()), 1)
            price_idx = next((i for i, h in enumerate(headers) if 'price' in h.lower() or 'last' in h.lower()), 2)
            change_idx = next((i for i, h in enumerate(headers) if 'change' in h.lower() and '%' not in h.lower()), 3)
            pct_change_idx = next((i for i, h in enumerate(headers) if '%' in h or ('change' in h.lower() and '%' in h.lower())), 4)
            
            print(f"Using column indices - Symbol: {symbol_idx}, Name: {name_idx}, Price: {price_idx}, Change: {change_idx}, % Change: {pct_change_idx}")
            
            for row in rows[1:]:  # Skip header row
                cols = row.find_all(['td', 'th'])
                if len(cols) >= max(symbol_idx, name_idx, price_idx, change_idx, pct_change_idx) + 1:
                    try:
                        symbol = cols[symbol_idx].text.strip()
                        name = cols[name_idx].text.strip() if name_idx < len(cols) else ""
                        price = cols[price_idx].text.strip()
                        change = cols[change_idx].text.strip()
                        percent_change = cols[pct_change_idx].text.strip()
                        
                        # Only add if we have a valid symbol and price
                        if symbol and price:
                            data.append({
                                "Symbol": symbol,
                                "Name": name,
                                "Price": price,
                                "Change": change,
                                "Change %": percent_change
                            })
                    except Exception as e:
                        print(f"Error processing row: {str(e)}")
                        continue
            
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

class WSJGainerProcess(GainerProcess):
    def __init__(self):
        super().__init__(source_name="wsj")
        self.csv_file = "wsjgainers.csv"
        self.norm_file = "wsjgainers_norm.csv"
    
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

        output_df['source'] = 'Wall Street Journal'
        output_df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if len(output_df.columns) != len(required_columns) + 2:
            raise AssertionError("Output columns don't match required format")
        if output_df.empty:
            raise AssertionError("process resulted in empty df")

        return output_df
    
    def normalize(self):
        print("Normalizing WSJ gainers")
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
            
            df["Source"] = "Wall Street Journal"
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
        print("Saving WSJ gainers with timestamp")
        try:
            # Check if file exists
            if not os.path.exists(self.norm_file):
                print(f"Error: Normalized CSV file not found: {self.norm_file}")
                return None
            
            # Create data directory if it doesn't exist
            os.makedirs("data", exist_ok=True)
            
            # Generate timestamped filename
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_file = f"data/wsjgainers_norm_{timestamp}.csv"
            
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
