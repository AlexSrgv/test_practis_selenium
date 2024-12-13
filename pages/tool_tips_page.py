from locators.tool_tips_page_locators import ToolTipsPageLocators
from pages.base_page import BasePage


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def hover_btn(self):
        elem = self.elment_is_visible(self.locators.TOOL_TIPS_BTN)
        self.action_move_to_element(elem)


    def get_text(self):
        text = self.elment_is_visible(self.locators.HOVER_MSG).text
        return text

    def get_css_property(self, property_name):
        data = self.elment_is_visible(self.locators.TOOL_TIPS_BTN)
        return data.value_of_css_property(property_name)

    def hover_word(self):
        elem = self.elment_is_visible(self.locators.WORD_LOC)
        self.action_move_to_element(elem)

    def word_get_text(self):
        text = self.elment_is_visible(self.locators.WORD_MSG_LOC).text
        return text

    def get_word_color(self,background_color):
        data = self.elment_is_visible(self.locators.WORD_LOC)
        return data.value_of_css_property(background_color)

    def hover_number(self):
        elem = self.elment_is_visible(self.locators.NUMBER_LOC)
        self.action_move_to_element(elem)

    def number_get_text(self):
        text = self.elment_is_visible(self.locators.NUMBER_MSG_LOC).text
        return text
