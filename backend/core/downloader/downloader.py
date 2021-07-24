from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass


class SIZE(Enum):
    LARGE = 1
    MEDIUM = 2
    SMALL = 3


@dataclass
class ACCDownloader(ABC):
    """Downloader class for downloading objects"""

    url: str
    size: SIZE = SIZE.LARGE

    @abstractmethod
    def download(self):
        NotImplementedError("Implement the download method")
