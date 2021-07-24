import pytest

from backend.core.downloader.downloader import SIZE
from backend.core.downloader.video_downloader import PexelsVideoDownloader
from backend.core.downloader.audio_downloader import BenSoundAudioDownloader

@pytest.fixture(scope='module')
def valid_large_video_downloader() -> PexelsVideoDownloader:
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268/'
    return PexelsVideoDownloader(url, SIZE.LARGE)

@pytest.fixture(scope='module')
def invalid_url_medium_video_downloader() -> PexelsVideoDownloader:
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268a/'
    return PexelsVideoDownloader(url, SIZE.MEDIUM)

@pytest.fixture(scope='module')
def invalid_id_medium_video_downloader() -> PexelsVideoDownloader:
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268123123/'
    return PexelsVideoDownloader(url, SIZE.MEDIUM)

@pytest.fixture(scope='module')
def valid_audio_downloader() -> BenSoundAudioDownloader:
    url = "https://www.bensound.com/royalty-free-music/track/better-days"
    return BenSoundAudioDownloader(url)

@pytest.fixture(scope='module')
def invalid_audio_downloader() -> BenSoundAudioDownloader:
    url = "https://www.bensound.com/royalty-free-music/track/better-days-123"
    return BenSoundAudioDownloader(url)