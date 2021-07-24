from dataclasses import dataclass
import re
from pathlib import Path
import shutil

import requests

from backend.core.downloader.downloader import ACCDownloader
from backend import config

PEXELS_SEARCH_API = "https://api.pexels.com/videos/search"
PEXELS_GET_VIDEO_API = "https://api.pexels.com/videos/videos/"


@dataclass
class PexelsVideoDownloader(ACCDownloader):
    """Class to download video files from Pexels"""

    def __post_init__(self):
        """parse id from URL"""
        founds = re.findall(r"([\d]+)[\/]*$", self.url)
        if len(founds) < 1:
            self.id = None
        else:
            self.id = founds[0]

    def download(self):
        """Implementation to download video"""
        if self.id is not None:
            video_url = self.get_download_url()
            if video_url is not None:
                filename = f"pexels-{self.id}.mp4"
                filepath = f"{config.get('PROJECT_PATH')}tmp/{filename}"
                self.save(video_url, filepath)
                return filepath
        return None

    def get_download_url(self) -> str:
        """Parse pexels API response and get download link based on size"""
        resp = requests.get(f"{PEXELS_GET_VIDEO_API}{self.id}", headers={
                "Authorization": config.get("PEXELS_API_KEY")
            })

        if resp.status_code != 200:
            return None

        resp_json = resp.json()
        videos = sorted(resp_json['video_files'], key=lambda i: i['width']
                        if i['width'] is not None else 0, reverse=True)
        if len(videos) > 0 and len(videos) > self.size.value:
            return videos[self.size.value]['link']
        return None
