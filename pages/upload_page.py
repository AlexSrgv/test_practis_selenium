from locators.upload_page_herokuapp_locator import UploadPageLocators
from pages.base_page import BasePage


class UploadPage(BasePage):
    locators = UploadPageLocators()

    def upload_file(self, file_path):
        self.elment_is_visible(self.locators.UPLOAD_BTN_LOCATOR).send_keys(file_path)
        self.elment_is_clicable(self.locators.SUBMIT_BTN).click()

    def check_upload_file(self):
        h3_text = self.elment_is_visible(self.locators.HEADER_TEXT_LOCATOR).text
        file_name = self.elment_is_visible(self.locators.UPLOAD_FILE_NAME_LOCATOR).text
        return h3_text, file_name
