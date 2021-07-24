from pathlib import Path

from backend.core.downloader.audio_downloader import BenSoundAudioDownloader
from backend.core.downloader.downloader import SIZE
from backend import config

def test_constructor(valid_audio_downloader: BenSoundAudioDownloader):
    url = "https://www.bensound.com/royalty-free-music/track/better-days"
    assert valid_audio_downloader.url == url
    # default size test
    assert valid_audio_downloader.size == SIZE.LARGE

def test_none_url(invalid_audio_downloader: BenSoundAudioDownloader):
    url = "https://www.bensound.com/royalty-free-music/track/better-days-123"
    assert invalid_audio_downloader.url == url
    # default size test
    assert invalid_audio_downloader.size == SIZE.LARGE


def test_download(valid_audio_downloader: BenSoundAudioDownloader):
    url = 'https://www.bensound.com/royalty-free-music/track/better-days'

    filepath = valid_audio_downloader.download()
    assert filepath is not None
    assert Path(filepath).is_file() == True
    assert Path(filepath).stat().st_size > 0


def test_download_error(invalid_audio_downloader: BenSoundAudioDownloader):
    url = "https://www.bensound.com/royalty-free-music/track/better-days-123"

    filepath = invalid_audio_downloader.download()
    assert filepath is None
