import shutil

import requests
from bs4 import BeautifulSoup

from backend.core.downloader.downloader import ACCDownloader
from backend import config
BASE_URL = 'https://www.bensound.com/'

class BenSoundAudioDownloader(ACCDownloader):
    """Class to download audio files"""

    def download(self) -> str:
        """Implementation to download audio"""
        
        file_url = self.get_download_url()
        if file_url is not None:
            download_link = f'{BASE_URL}{file_url}'
            filename = file_url.split('/')[1]
            filepath = f"{config.get('PROJECT_PATH')}tmp/{filename}"
            self.save(download_link, filepath)
            return filepath
        return None
    
    def get_download_url(self) -> str:
        """Parse web content from audio details page to find download URL"""
        audio_res = requests.get(self.url)
        bs = BeautifulSoup(audio_res.content, 'html.parser')
        license_section = bs.find(id='freelicense')
        if license_section is not None:
            link = license_section.find('a', string="Download")
            if link is not None:
                return link['href']
        return None