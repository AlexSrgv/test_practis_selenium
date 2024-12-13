import time

from data.urls import Urls
from pages.tool_tips_page import ToolTipsPage


class TestToolTips:
    url = Urls()


    def test_hover_btn(self, driver):
        page = ToolTipsPage(driver, self.url.demoqa_tool_tips_url)
        page.open()
        page.hover_btn()
        text = page.get_text()
        assert text == 'You hovered over the Button'

    def test_get_cursor(self, driver):
        page = ToolTipsPage(driver, self.url.demoqa_tool_tips_url)
        page.open()
        page.hover_btn()
        property_value = page.get_css_property('cursor')
        assert property_value == 'pointer'

    def test_get_color(self, driver):
        page = ToolTipsPage(driver, self.url.demoqa_tool_tips_url)
        page.open()
        property_value_before = page.get_css_property('background-color')
        page.hover_btn()
        property_value_after = page.get_css_property('background-color')
        assert property_value_before != property_value_after

    def test_hover_word(self, driver):
        page = ToolTipsPage(driver, self.url.demoqa_tool_tips_url)
        page.open()
        page.hover_word()
        text = page.word_get_text()
        assert text == 'You hovered over the Contrary'

    def test_word_color(self, driver):
        page = ToolTipsPage(driver, self.url.demoqa_tool_tips_url)
        page.open()
        page.hover_word()
        word_color_after = page.get_word_color('background_color')
        assert  word_color_after != "rgb(0 123 255)"

    def test_number_hover(self, driver):
        page = ToolTipsPage(driver, self.url.demoqa_tool_tips_url)
        page.open()
        page.hover_number()
        text = page.number_get_text()
        assert text == 'You hovered over the 1.10.32'