#!/usr/bin/env python3
"""
Script to download and process stock gainer data from various sources.
Uses a template method pattern to standardize the process across different sources.
"""

import os
import sys
import argparse
import datetime
from bin.gainers.factory import GainerFactory

class GainerTemplate:
    """Template class for the gainer download and processing workflow."""
    
    def __init__(self, source_type, timestamp=None):
        """
        Initialize with the source type and optional timestamp.
        
        Args:
            source_type (str): Type of source ("yahoo" or "wsj").
            timestamp (str, optional): Timestamp to use in filenames.
        """
        self.source_type = source_type
        self.timestamp = timestamp
        self.downloader = GainerFactory.create_downloader(source_type)
        self.processor = GainerFactory.create_processor(source_type)
    
    def execute(self, output_dir="data"):
        """
        Execute the full download and processing workflow.
        
        Args:
            output_dir (str): Directory to store the output files.
            
        Returns:
            str: Path to the final CSV file if successful, None otherwise.
        """
        print(f"Starting gainer data collection for {self.source_type}")
        
        # Step 1: Download the data
        csv_file = self.downloader.download()
        if not csv_file:
            print(f"Error: Failed to download data from {self.source_type}")
            return None
        
        # Step 2: Normalize the data
        norm_file = self.processor.normalize()
        if not norm_file:
            print(f"Error: Failed to normalize data from {self.source_type}")
            return None
        
        # Step 3: Save with timestamp
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate timestamp if not provided
        timestamp = self.timestamp
        if not timestamp:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Define the output filename
        if self.source_type == "yahoo":
            output_file = f"{output_dir}/ygainers_norm_{timestamp}.csv"
        else:
            output_file = f"{output_dir}/wsjgainers_norm_{timestamp}.csv"
        
        # Load the normalized data
        try:
            import pandas as pd
            df = pd.read_csv(self.processor.norm_file)
            df.to_csv(output_file, index=False)
            print(f"Saved timestamped file: {output_file}")
        except Exception as e:
            print(f"Error saving timestamped file: {str(e)}")
            return None
        
        print(f"Successfully processed {self.source_type} gainer data")
        print(f"Final output: {output_file}")
        
        return output_file

def main():
    """Main function to parse arguments and run the gainer template."""
    parser = argparse.ArgumentParser(description="Download and process stock gainer data.")
    parser.add_argument("--source", "-s", type=str, required=True, 
                        choices=["yahoo", "wsj"],
                        help="Source of gainer data (yahoo or wsj)")
    parser.add_argument("--timestamp", "-t", type=str,
                        help="Custom timestamp to use in filenames (format: YYYYMMDD_HHMMSS)")
    parser.add_argument("--output-dir", "-o", type=str, default="data",
                        help="Directory to store output files")
    
    args = parser.parse_args()
    
    # Create and execute the template
    template = GainerTemplate(args.source, args.timestamp)
    result = template.execute(output_dir=args.output_dir)
    
    if result:
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())
