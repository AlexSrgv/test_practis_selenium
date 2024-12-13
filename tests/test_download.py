import time

from pages.DownLoadPage import DownLoadPage
from data.urls import Urls

class TestDownload:
    url = Urls()


    def test_download(self, driver):
        page = DownLoadPage(driver, f"{self.url.herokuapp_base_url}download")
        page.open()
        page.download_file()
        time.sleep(5)