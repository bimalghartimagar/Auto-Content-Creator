# Test Pexels Video Downloader
from backend.core.downloader.downloader import SIZE
from backend.core.downloader.video_downloader import PexelsVideoDownloader
from pathlib import Path
from backend import config

def test_constructor(valid_large_video_downloader):
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268/'
    assert valid_large_video_downloader.url == url
    assert valid_large_video_downloader.size == SIZE.LARGE


def test_id_creation(valid_large_video_downloader):
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268/'
    assert valid_large_video_downloader.url == url
    assert valid_large_video_downloader.size == SIZE.LARGE
    assert valid_large_video_downloader.id == '4154268'


def test_none_id_creation(invalid_medium_video_downloader):
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268a/'
    assert invalid_medium_video_downloader.url == url
    assert invalid_medium_video_downloader.size == SIZE.MEDIUM
    assert invalid_medium_video_downloader.id == None


def test_download(valid_large_video_downloader):
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268/'
    assert valid_large_video_downloader.url == url
    assert valid_large_video_downloader.size == SIZE.LARGE
    assert valid_large_video_downloader.id == '4154268'
    
    filename = valid_large_video_downloader.download()
    
    assert filename == 'pexels-4154268.mp4'
    filepath = f"{config.get('PROJECT_PATH')}tmp/{filename}"
    assert Path(filepath).is_file() == True
    assert Path(filepath).stat().st_size > 0

def test_download_error(invalid_medium_video_downloader):
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268a/'
    assert invalid_medium_video_downloader.url == url
    assert invalid_medium_video_downloader.size == SIZE.MEDIUM
    assert invalid_medium_video_downloader.id is None
    filename = invalid_medium_video_downloader.download()
    assert filename is None
