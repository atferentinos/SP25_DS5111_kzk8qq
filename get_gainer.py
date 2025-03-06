#!/usr/bin/env python3
"""
Script to download and process stock gainer data from various sources.
Uses a template method pattern to standardize the process across different sources.
"""

import os
import sys
import argparse
from bin.gainers.factory import GainerFactory

class GainerTemplate:
    """Template class for the gainer download and processing workflow."""
    
    def __init__(self, source_type):
        """
        Initialize with the source type.
        
        Args:
            source_type (str): Type of source ("yahoo" or "wsj").
        """
        self.source_type = source_type
        self.downloader = GainerFactory.create_downloader(source_type)
        self.processor = GainerFactory.create_processor(source_type)
    
    def execute(self):
        """
        Execute the full download and processing workflow.
        
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
        final_file = self.processor.save_with_timestamp()
        if not final_file:
            print(f"Error: Failed to save timestamped data from {self.source_type}")
            return None
        
        print(f"Successfully processed {self.source_type} gainer data")
        print(f"Final output: {final_file}")
        
        return final_file

def main():
    """Main function to parse arguments and run the gainer template."""
    parser = argparse.ArgumentParser(description="Download and process stock gainer data.")
    parser.add_argument("--source", "-s", type=str, required=True, 
                        choices=["yahoo", "wsj"],
                        help="Source of gainer data (yahoo or wsj)")
    
    args = parser.parse_args()
    
    # Create and execute the template
    template = GainerTemplate(args.source)
    result = template.execute()
    
    if result:
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())
