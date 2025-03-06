from bin.gainers.yahoo import YahooGainerDownload, YahooGainerProcess
from bin.gainers.wsj import WSJGainerDownload, WSJGainerProcess

class GainerFactory:
    """Factory class to create appropriate gainer objects."""
    
    @staticmethod
    def create_downloader(source_type):
        """
        Create a downloader object based on source type.
        
        Args:
            source_type (str): Type of source ("yahoo" or "wsj").
            
        Returns:
            GainerDownload: A downloader object.
            
        Raises:
            ValueError: If source_type is not supported.
        """
        if source_type.lower() == "yahoo":
            return YahooGainerDownload()
        elif source_type.lower() == "wsj":
            return WSJGainerDownload()
        else:
            raise ValueError(f"Unsupported source type: {source_type}")
    
    @staticmethod
    def create_processor(source_type):
        """
        Create a processor object based on source type.
        
        Args:
            source_type (str): Type of source ("yahoo" or "wsj").
            
        Returns:
            GainerProcess: A processor object.
            
        Raises:
            ValueError: If source_type is not supported.
        """
        if source_type.lower() == "yahoo":
            return YahooGainerProcess()
        elif source_type.lower() == "wsj":
            return WSJGainerProcess()
        else:
            raise ValueError(f"Unsupported source type: {source_type}")
