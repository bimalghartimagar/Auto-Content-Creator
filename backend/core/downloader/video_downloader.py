from dataclasses import dataclass
import re

from backend.core.downloader.downloader import ACCDownloader

PEXELS_SEARCH_API = 'https://api.pexels.com/videos/search'
PEXELS_GET_VIDEO_API = 'https://api.pexels.com/videos/videos/'

@dataclass
class PexelsVideoDownloader(ACCDownloader):
    """Class to download video files from Pexels"""

    def __post_init__(self):
        """parse id from URL"""
        founds = re.findall(r'([\d]+)[\/]*$', self.url)
        if len(founds) < 1:
            self.id = None
        else:
            self.id = founds[0]

    def download(self):
        """Implementation to download video"""
        pass
