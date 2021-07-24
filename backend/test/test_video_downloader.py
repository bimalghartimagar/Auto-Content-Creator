# Test Pexels Video Downloader


from backend.core.downloader.downloader import SIZE
from backend.core.downloader.video_downloader import PexelsVideoDownloader


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
    downloader = PexelsVideoDownloader(url, SIZE.MEDIUM)
    assert downloader.url == url
    assert downloader.size == SIZE.MEDIUM
    assert downloader.id == None
