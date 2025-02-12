import sys
import pytest
import pandas as pd
from pathlib import Path
sys.path.append('.')
import bin.normalize_csv as normalize

def test_validate_csv_path(tmp_path):
   valid_csv = tmp_path / "test.csv"
   valid_csv.write_text("dummy data")
   assert normalize.validate_csv_path(str(valid_csv)) == valid_csv
   
   invalid_file = tmp_path / "test.txt"
   invalid_file.write_text("dummy data")
   with pytest.raises(AssertionError):
       normalize.validate_csv_path(str(invalid_file))
   
   with pytest.raises(AssertionError):
       normalize.validate_csv_path("nonexistent.csv")

def test_transform_stock_data():
   input_data = {
       'Symbol': ['AAPL', 'GOOGL'],
       'Price': [150.0, 2800.0],
       'Change': [-2.0, 5.0],
       'Change %': ['-1.3%', '0.18%']
   }
   input_df = pd.DataFrame(input_data)
   
   result = normalize.transform_stock_data(input_df)
   
   expected_columns = ['symbol', 'price', 'price_change', 'price_percent_change']
   assert list(result.columns) == expected_columns
   
   assert result['symbol'].tolist() == ['AAPL', 'GOOGL']

def test_save_normalized_csv(tmp_path):
   df = pd.DataFrame({
       'symbol': ['AAPL'],
       'price': [150.0],
       'price_change': [-2.0],
       'price_percent_change': ['-1.3%']
   })
   
   output_path = tmp_path / "test_output.csv"
   normalize.save_normalized_csv(df, output_path)
   assert output_path.exists()
   
   loaded_df = pd.read_csv(output_path)
   assert list(loaded_df.columns) == list(df.columns)
