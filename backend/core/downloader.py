from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass


class SIZE(Enum):
    LARGE = 'large'
    MEDIUM = 'medium'
    SMALL = 'small'


@dataclass
class ACCDownloader(ABC):
    """Downloader class for downloading objects"""

    url: str
    size: SIZE

    @abstractmethod
    def download(self):
        NotImplementedError("Implement the download method")
