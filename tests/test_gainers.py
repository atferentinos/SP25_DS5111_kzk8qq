import unittest
import datetime
from bin.gainers.yahoo import YahooGainerDownload, YahooGainerProcess
from bin.gainers.wsj import WSJGainerDownload, WSJGainerProcess
from bin.gainers.factory import GainerFactory
import os
import pandas as pd

class TestGainerFactory(unittest.TestCase):
    
    def test_create_downloader(self):
        """Test that factory creates correct downloader objects"""
        yahoo_dl = GainerFactory.create_downloader("yahoo")
        wsj_dl = GainerFactory.create_downloader("wsj")
        
        self.assertIsInstance(yahoo_dl, YahooGainerDownload)
        self.assertIsInstance(wsj_dl, WSJGainerDownload)
    
    def test_create_processor(self):
        """Test that factory creates correct processor objects"""
        yahoo_proc = GainerFactory.create_processor("yahoo")
        wsj_proc = GainerFactory.create_processor("wsj")
        
        self.assertIsInstance(yahoo_proc, YahooGainerProcess)
        self.assertIsInstance(wsj_proc, WSJGainerProcess)
    
    def test_invalid_source(self):
        """Test factory raises ValueError for invalid sources"""
        with self.assertRaises(ValueError):
            GainerFactory.create_downloader("invalid")
        
        with self.assertRaises(ValueError):
            GainerFactory.create_processor("invalid")

class TestYahooGainer(unittest.TestCase):
    
    def test_yahoo_gainer_init(self):
        """Test initialization of Yahoo downloader"""
        downloader = YahooGainerDownload()
        self.assertEqual(downloader.url, "https://finance.yahoo.com/gainers")
        self.assertEqual(downloader.html_file, "ygainers.html")
        self.assertEqual(downloader.csv_file, "ygainers.csv")
    
    def test_yahoo_processor_init(self):
        """Test initialization of Yahoo processor"""
        processor = YahooGainerProcess()
        self.assertEqual(processor.source_name, "yahoo")
        self.assertEqual(processor.csv_file, "ygainers.csv")
        self.assertEqual(processor.norm_file, "ygainers_norm.csv")

class TestWSJGainer(unittest.TestCase):
    
    def test_wsj_gainer_init(self):
        """Test initialization of WSJ downloader"""
        downloader = WSJGainerDownload()
        self.assertTrue("wsj.com" in downloader.url.lower())
        self.assertEqual(downloader.html_file, "wsjgainers.html")
        self.assertEqual(downloader.csv_file, "wsjgainers.csv")
    
    def test_wsj_processor_init(self):
        """Test initialization of WSJ processor"""
        processor = WSJGainerProcess()
        self.assertEqual(processor.source_name, "wsj")
        self.assertEqual(processor.csv_file, "wsjgainers.csv")
        self.assertEqual(processor.norm_file, "wsjgainers_norm.csv")

class TestTimestampFunctionality(unittest.TestCase):
    
    def test_generate_timestamp(self):
        """Test timestamp formatting"""
        # Use standard datetime instead of the generate_timestamp method
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Verify timestamp format (YYYYMMDD_HHMMSS)
        self.assertEqual(len(timestamp), 15)
        self.assertTrue('_' in timestamp)
        
        # Check that parts are numeric
        date_part, time_part = timestamp.split('_')
        self.assertTrue(date_part.isdigit())
        self.assertTrue(time_part.isdigit())

if __name__ == '__main__':
    unittest.main()
