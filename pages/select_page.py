from selenium.webdriver.support.select import Select

from locators.select_page_locators import SelectPageLocators
from pages.base_page import BasePage


class SelectPage(BasePage):
    locators = SelectPageLocators()


    def select(self, value:str):
        select = Select(self.elment_is_visible(self.locators.OLD_STILY_SELECT_MENU_LOC))
        select.select_by_visible_text(value)