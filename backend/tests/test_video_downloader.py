# Test Pexels Video Downloader
from backend.core.downloader.downloader import SIZE
from backend.core.downloader.video_downloader import PexelsVideoDownloader
from pathlib import Path
from backend import config

def test_constructor():
    url = 'http://www.test.com'
    downloader = PexelsVideoDownloader(url)
    assert downloader.url == 'http://www.test.com'
    assert downloader.size == SIZE.LARGE


def test_id_creation():
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268/'
    downloader = PexelsVideoDownloader(url, SIZE.MEDIUM)
    assert downloader.url == url
    assert downloader.size == SIZE.MEDIUM
    assert downloader.id == '4154268'


def test_none_id_creation():
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268a/'
    downloader = PexelsVideoDownloader(url, SIZE.SMALL)
    assert downloader.url == url
    assert downloader.size == SIZE.SMALL
    assert downloader.id == None


def test_download():
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268/'
    downloader = PexelsVideoDownloader(url, SIZE.LARGE)
    
    assert downloader.url == url
    assert downloader.size == SIZE.LARGE
    assert downloader.id == '4154268'
    
    filename = downloader.download()
    
    assert filename == 'pexels-4154268.mp4'
    filepath = f"{config.get('PROJECT_PATH')}tmp/{filename}"
    assert Path(filepath).is_file() == True
    assert Path(filepath).stat().st_size > 0

def test_download_error():
    url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268a/'
    downloader = PexelsVideoDownloader(url, SIZE.LARGE)
    filename = downloader.download()
    assert downloader.url == url
    assert downloader.size == SIZE.LARGE
    assert filename is None
    assert downloader.id is None