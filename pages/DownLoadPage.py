from locators.download_page_herokuapp_locator import DownloadPageLocators
from pages.base_page import BasePage


class DownLoadPage(BasePage):
    locators = DownloadPageLocators()

    def download_file(self):
        self.elment_is_visible(self.locators.DOWNLOAD_LOCATOR).click()
