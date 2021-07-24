import pytest

from backend.core.downloader.downloader import SIZE
from backend.core.downloader.video_downloader import PexelsVideoDownloader

@pytest.fixture(scope='module')
def valid_large_video_downloader():
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268/'
    return PexelsVideoDownloader(url, SIZE.LARGE)

@pytest.fixture(scope='module')
def invalid_medium_video_downloader():
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268a/'
    return PexelsVideoDownloader(url, SIZE.MEDIUM)


