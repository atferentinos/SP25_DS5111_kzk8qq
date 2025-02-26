from bin.gainers.base import GainerDownload, GainerProcess
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import time

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        super().__init__(url="https://www.wsj.com/market-data/stocks/marketsdiary")
        self.html_file = "wsj_gainers.html"
        self.csv_file = "wsj_gainers.csv"
    
    def download(self):
        print("Downloading WSJ gainers")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/58.0.3029.110"
        }
        response = requests.get(self.url, headers=headers)
        
        with open(self.html_file, "w", encoding="utf-8") as f:
            f.write(response.text)
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        gainers_section = soup.find("div", {"id": "market_diary_gainers"})
        
        data = []
        
        if gainers_section:
            table = gainers_section.find("table")
            if table:
                rows = table.find_all("tr")
                for row in rows[1:]:  # Skip header row
                    cols = row.find_all("td")
                    if len(cols) >= 4:
                        symbol = cols[0].text.strip()
                        price = cols[1].text.strip()
                        change = cols[2].text.strip()
                        percent_change = cols[3].text.strip()
                        
                        data.append({
                            "Symbol": symbol,
                            "Price": price,
                            "Change": change,
                            "% Change": percent_change
                        })
        
        df = pd.DataFrame(data)
        
        df.to_csv(self.csv_file, index=False)
        return self.csv_file

class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        super().__init__()
        self.csv_file = "wsj_gainers.csv"
        self.norm_file = "wsj_gainers_norm.csv"
    
    def normalize(self):
        print("Normalizing WSJ gainers")
        df = pd.read_csv(self.csv_file)
        
        df["Price"] = df["Price"].str.replace("$", "").astype(float)
        
        df["Change"] = df["Change"].str.replace("+", "").str.replace("-", "-").astype(float)
        df["% Change"] = df["% Change"].str.replace("%", "").str.replace("+", "").astype(float)
        
        df["Source"] = "Wall Street Journal"
        
        df["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        df.to_csv(self.norm_file, index=False)
        return self.norm_file
    
    def save_with_timestamp(self):
        print("Saving WSJ gainers")
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_file = f"wsj_gainers_norm_{timestamp}.csv"
        
        df = pd.read_csv(self.norm_file)
        
        df.to_csv(output_file, index=False)
        
        print(f"Saved timestamped file: {output_file}")
        return output_file
