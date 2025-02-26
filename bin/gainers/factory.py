from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ
from bin.gainers.mock import GainerDownloadMock, GainerProcessMock

class GainerFactory:
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice 
    
    def get_downloader(self):
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()
        elif self.choice == 'test':
            return GainerDownloadMock()
    
    def get_processor(self):
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()
        elif self.choice == 'test':
            return GainerProcessMock()
