import random
import time

from data.urls import Urls
from pages.drag_and_drop_page import DragAndDroppPage


class TestDraAndDropp:
    url = Urls()


    def test_drag_and_drop(self, driver):
        page = DragAndDroppPage(driver, self.url.demoqa_droppable_url)
        page.open()
        page.drag_and_drop1()
        text = page.get_text()
        assert text == "Dropped!"

    def test_drag_by_offset(self, driver):
        page = DragAndDroppPage(driver, self.url.demoqa_draggable_url)
        page.open()
        coord_before, coord_after = page.draggable(200,100)
        assert coord_before != coord_after


