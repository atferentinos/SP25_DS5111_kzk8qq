#!/usr/bin/env python3

import sys
import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_csv_path(file_path):
    assert isinstance(file_path, str), f"Expected string path, got {type(file_path)}"
    
    path = Path(file_path)
    assert path.exists(), f"File does not exist: {file_path}"
    assert path.suffix.lower() == '.csv', f"File must be a CSV, got: {path.suffix}"
    
    return path

def transform_stock_data(input_df):
    assert isinstance(input_df, pd.DataFrame), f"Expected DataFrame, got {type(input_df)}"
    assert not input_df.empty, "Input DataFrame is empty"
    
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
    assert not missing_cols, f"Missing required columns: {missing_cols}"
    
    output_df = output_df[required_columns]
    
    assert len(output_df.columns) == len(required_columns), "Output columns don't match required format"
    assert not output_df.empty, "process resulted in empty df"
    
    return output_df

def save_normalized_csv(df, output_path):
    assert isinstance(df, pd.DataFrame), f"Expected DataFrame, got {type(df)}"
    assert isinstance(output_path, Path), f"Expected Path, got {type(output_path)}"
    
    df.to_csv(output_path, index=False)
    
    assert output_path.exists(), f"Failed to create output file: {output_path}"

def main():
    if len(sys.argv) != 2:
        logger.error("Usage: python normalize_csv.py <input_csv_path>")
        sys.exit(1)

    try:
        input_path = validate_csv_path(sys.argv[1])
        output_path = input_path.with_name(f"{input_path.stem}_norm.csv")
        
        logger.info(f"Reading CSV from {input_path}")
        input_df = pd.read_csv(input_path)
        
        normalized_df = transform_stock_data(input_df)
        
        save_normalized_csv(normalized_df, output_path)
        logger.info(f"Normalized CSV saved to {output_path}")
        
    except AssertionError as e:
        logger.error(f"Validation error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error processing CSV: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
