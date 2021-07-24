from dataclasses import dataclass
from downloader import ACCDownloader


@dataclass
class VideoDownloader(ACCDownloader):
    """Class to download video files"""

    def download(self):
        """Implementation to download video"""
        pass
