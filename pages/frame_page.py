from locators.frame_page_locators import FramePageLocators
from pages.base_page import BasePage


class FramePage(BasePage):
    locators = FramePageLocators()

    def check_frame(self, frame_name):
        if frame_name == 'frame1':
            frame = self.elment_is_present(self.locators.BIG_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.elment_is_present(self.locators.FRAME_PAGE).text
            self.driver.switch_to.default_content()
            return [width, height, text]
        if frame_name == 'frame2':
            frame = self.elment_is_present(self.locators.SMALL_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.elment_is_present(self.locators.FRAME_PAGE).text
            self.driver.switch_to.default_content()
            return [width, height, text]