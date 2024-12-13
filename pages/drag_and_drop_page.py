from locators.drag_and_drop_page_locators import DragAndDropLocators
from pages.base_page import BasePage


class DragAndDroppPage(BasePage):

    locators = DragAndDropLocators()


    def drag_and_drop1(self):
        source_elem = self.elment_is_visible(self.locators.DRAG_ME_LOC)
        target_elem = self.elment_is_visible(self.locators.DROP_ME_LOC)
        self.action_drag_and_drop(source_elem, target_elem)


    def get_text(self):
        text = self.elment_is_visible(self.locators.DROP_ME_TEXT_LOC).text
        return text

    def draggable(self, xoffset, yoffset):
        elem = self.elment_is_visible(self.locators.DRAG_LOC)
        coord_before = elem.location
        self.action_drag_and_drop_offset(elem, xoffset, yoffset)
        coord_after = elem.location
        return coord_before, coord_after


