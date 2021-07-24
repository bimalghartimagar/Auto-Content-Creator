from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
import shutil

import requests


class SIZE(Enum):
    LARGE = 0
    MEDIUM = 2
    SMALL = 2


@dataclass
class ACCDownloader(ABC):
    """Downloader class for downloading objects"""

    url: str
    size: SIZE = SIZE.LARGE

    def save(self, download_link, filepath):
        with requests.get(download_link, stream=True) as req:
            with open(filepath, 'wb') as f:
                shutil.copyfileobj(req.raw, f)

    @abstractmethod
    def download(self) -> str:
        NotImplementedError("Implement the download method")

    @abstractmethod
    def get_download_url(self) -> str:
        NotImplementedError("Implement the get_download_url method")
