import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from pathlib import Path
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bin.gainers.factory import GainerFactory
from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ
from bin.gainers.mock import GainerDownloadMock, GainerProcessMock

class TestGainerFactory(unittest.TestCase):
    """Test the GainerFactory class"""
    
    def test_factory_yahoo(self):
        """Test factory creates correct Yahoo objects"""
        factory = GainerFactory('yahoo')
        downloader = factory.get_downloader()
        processor = factory.get_processor()
        
        self.assertIsInstance(downloader, GainerDownloadYahoo)
        self.assertIsInstance(processor, GainerProcessYahoo)
    
    def test_factory_wsj(self):
        """Test factory creates correct WSJ objects"""
        factory = GainerFactory('wsj')
        downloader = factory.get_downloader()
        processor = factory.get_processor()
        
        self.assertIsInstance(downloader, GainerDownloadWSJ)
        self.assertIsInstance(processor, GainerProcessWSJ)
    
    def test_factory_invalid(self):
        """Test factory raises error for invalid source"""
        with self.assertRaises(AssertionError):
            GainerFactory('invalid')
            
    def test_factory_mock(self):
        """Test factory creates correct Mock objects"""
        factory = GainerFactory('test')
        downloader = factory.get_downloader()
        processor = factory.get_processor()

        self.assertIsInstance(downloader, GainerDownloadMock)
        self.assertIsInstance(processor, GainerProcessMock)

    def test_mock_download_no_network(self):
        """Test mock downloader works without network"""
        downloader = GainerDownloadMock()
        csv_file = downloader.download()

        self.assertTrue(os.path.exists(csv_file))

        df = pd.read_csv(csv_file)
        self.assertIn("TEST1", df["Symbol"].values)

class TestGainerProcessYahoo(unittest.TestCase):
    """Test Yahoo processor implementation"""
    
    def setUp(self):
        """Set up test environment"""
        # Create test CSV file
        self.test_csv = "test_yahoo_gainers.csv"
        test_data = {
            "Symbol": ["AAPL", "MSFT", "GOOGL"],
            "Price": ["150.00", "300.00", "2000.00"],
            "Change": ["+2.00", "+4.50", "-10.00"],
            "Change %": ["+1.35%", "+1.52%", "-0.50%"]
        }
        pd.DataFrame(test_data).to_csv(self.test_csv, index=False)
        
        self.processor = GainerProcessYahoo()
        self.processor.csv_file = self.test_csv
    
    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)
        
        norm_file = self.test_csv.replace(".csv", "_norm.csv")
        if os.path.exists(norm_file):
            os.remove(norm_file)
            
        for file in os.listdir():
            if file.startswith("test_yahoo_gainers_norm_") and file.endswith(".csv"):
                os.remove(file)
    
    def test_validate_csv_path(self):
        """Test CSV path validation"""
        # Valid CSV
        path = self.processor.validate_csv_path(self.test_csv)
        self.assertIsInstance(path, Path)
        
        # Non-existent file
        with self.assertRaises(AssertionError):
            self.processor.validate_csv_path("nonexistent.csv")
        
        # Non-CSV file
        with self.assertRaises(AssertionError):
            open("test.txt", "w").close()
            self.processor.validate_csv_path("test.txt")
            os.remove("test.txt")
    
    def test_transform_stock_data(self):
        """Test stock data transformation"""
        df = pd.read_csv(self.test_csv)
        transformed = self.processor.transform_stock_data(df)
        
        self.assertIn('symbol', transformed.columns)
        self.assertIn('price', transformed.columns)
        self.assertIn('price_change', transformed.columns)
        self.assertIn('price_percent_change', transformed.columns)
        self.assertIn('source', transformed.columns)
        self.assertIn('timestamp', transformed.columns)
        
        self.assertEqual(transformed['source'].iloc[0], 'Yahoo Finance')

if __name__ == '__main__':
    unittest.main()
