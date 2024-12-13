from locators.buttons_page_locators import ButtonPageLocators
from pages.base_page import BasePage


class ButtonsPage(BasePage):
    locators = ButtonPageLocators()


    def double_click_btn(self):
        elem = self.elment_is_clicable(self.locators.DOUBLE_CLK_BTN_LOC)
        self.double_click(elem)
        text = self.elment_is_visible(self.locators.DOUBLE_CLK_TEXT_LOC).text
        return text

    def right_click_btn(self):
        elem = self.elment_is_clicable(self.locators.RIGHT_CLK_BTN_LOC)
        self.right_click(elem)
        text = self.elment_is_visible(self.locators.RIGHT_BTN_TEXT_LOC).text
        return text

    def click_btn(self):
        elem = self.elment_is_clicable(self.locators.CLK_BTN_LOC)
        elem.click()
        text = self.elment_is_visible(self.locators.CLK_TEXT_LOC).text
        return text
