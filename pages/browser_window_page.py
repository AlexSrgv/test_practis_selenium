from locators.browser_page_window_loc import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowsPageLocators()


    def check_open_new_tab(self):
        self.elment_is_visible(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.elment_is_visible(self.locators.NEW_TAB_PAGE).text
        return text_title


    def check_open_new_window(self):
        self.elment_is_visible(self.locators.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.elment_is_visible(self.locators.NEW_TAB_PAGE).text
        return text_title