# Test Pexels Video Downloader
from pathlib import Path

import pytest

from backend.core.downloader.downloader import SIZE
from backend.core.downloader.video_downloader import PexelsVideoDownloader
from backend import config

def test_constructor(valid_large_video_downloader: PexelsVideoDownloader):
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268/'
    assert valid_large_video_downloader.url == url
    assert valid_large_video_downloader.size == SIZE.LARGE

def test_id_creation(valid_large_video_downloader: PexelsVideoDownloader):
    assert valid_large_video_downloader.id == '4154268'

def test_none_id_creation(invalid_url_medium_video_downloader: PexelsVideoDownloader):
    assert invalid_url_medium_video_downloader.id == None

def test_download(valid_large_video_downloader: PexelsVideoDownloader):
    filename = 'pexels-4154268.mp4'
    path = f"{config.get('PROJECT_PATH')}tmp/{filename}"
    filepath = valid_large_video_downloader.download()
    assert filepath == path
    assert Path(filepath).is_file() == True
    assert Path(filepath).stat().st_size > 0

def test_download_error(invalid_url_medium_video_downloader: PexelsVideoDownloader):
    filepath = invalid_url_medium_video_downloader.download()
    assert filepath is None

def test_invalid_id_download_error(invalid_id_medium_video_downloader: PexelsVideoDownloader):
    filepath  = invalid_id_medium_video_downloader.download()
    assert filepath is None