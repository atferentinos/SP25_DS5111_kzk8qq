#!/usr/bin/env python3
"""
Lab 3 Code  for normalizing CSV files containing stock data.
Converts input CSV files to a standardized format with normalized column names.
"""

import sys
from pathlib import Path
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_csv_path(file_path):
    """
    Validate the input CSV file path.

    Args:
        file_path (str): Path to the CSV file

    Returns:
        Path: Validated Path object

    Raises:
        AssertionError: If path is invalid or file is not CSV
    """
    if not isinstance(file_path, str):
        raise AssertionError(f"Expected string path, got {type(file_path)}")
    path = Path(file_path)
    if not path.exists():
        raise AssertionError(f"File does not exist: {file_path}")
    if path.suffix.lower() != '.csv':
        raise AssertionError(f"File must be a CSV, got: {path.suffix}")
    return path

def transform_stock_data(input_df):
    """
    Change  stock data DataFrame to normalized format.

    Args:
        input_df (pd.DataFrame): Input DataFrame with data

    Returns:
        pd.DataFrame: Normalized DataFrame

    Raises:
        AssertionError: If DataFrame format is invalid
    """
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

    if len(output_df.columns) != len(required_columns):
        raise AssertionError("Output columns don't match required format")
    if output_df.empty:
        raise AssertionError("process resulted in empty df")

    return output_df

def save_normalized_csv(df, output_path):
    """
    Save DF to CSV.

    Args:
        df (pd.DataFrame): DataFrame to save
        output_path (Path): Path to save CSV file

    Raises:
        AssertionError: If save operation fails
    """
    if not isinstance(df, pd.DataFrame):
        msg = f"Expected DataFrame, got {type(df)}"
        raise AssertionError(msg)
    if not isinstance(output_path, Path):
        msg = f"Expected Path, got {type(output_path)}"
        raise AssertionError(msg)

    df.to_csv(output_path, index=False)

    if not output_path.exists():
        msg = f"Failed to create output file: {output_path}"
        raise AssertionError(msg)

def main():
    """Main function to process and normalize CSV file."""
    if len(sys.argv) != 2:
        logger.error("Usage: python normalize_csv.py <input_csv_path>")
        sys.exit(1)

    try:
        input_path = validate_csv_path(sys.argv[1])
        output_path = input_path.with_name(f"{input_path.stem}_norm.csv")

        logger.info("Reading CSV from %s", input_path)
        input_df = pd.read_csv(input_path)
        normalized_df = transform_stock_data(input_df)
        save_normalized_csv(normalized_df, output_path)
        logger.info("Normalized CSV saved to %s", output_path)

    except AssertionError as e:
        logger.error("Validation error: %s", str(e))
        sys.exit(1)
    except (pd.errors.EmptyDataError, IOError, ValueError) as e:
        logger.error("Error processing CSV: %s", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
