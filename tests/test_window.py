import time

from data.urls import Urls
from pages.browser_window_page import BrowserWindowPage



class TestWindowPage:
    url = Urls()

    def test_window_new_tab(self,driver):
        page = BrowserWindowPage(driver, self.url.demoqa_window_url)
        page.open()
        new_text = page.check_open_new_tab()
        assert new_text == 'This is a sample page'
        time.sleep(5)

    def test_window_new_window(self, driver):
        page = BrowserWindowPage(driver, self.url.demoqa_window_url)
        page.open()
        text_new_window = page.check_open_new_window()
        assert text_new_window == 'This is a sample page'