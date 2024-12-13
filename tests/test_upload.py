import time

from data.urls import Urls
from functions import get_root_path
from pages.upload_page import UploadPage


class TestUpload:
    url = Urls()

    def test_upload_file(self, driver):
        file_path = get_root_path('data/upload/subidaFoto.png')
        page = UploadPage(driver, f'{self.url.herokuapp_base_url}upload')
        page.open()
        page.upload_file(file_path)
        h3_text, file_name_text = page.check_upload_file()
        assert h3_text == "File Uploaded!"
        assert file_name_text == "subidaFoto.png"