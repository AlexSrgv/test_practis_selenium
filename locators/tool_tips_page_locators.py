

class ToolTipsPageLocators:

    TOOL_TIPS_BTN = ("css selector", "button[id='toolTipButton']")
    HOVER_MSG = ("css selector", "div[class='tooltip-inner']")
    WORD_LOC = ("xpath", "//a[text() = 'Contrary']")
    WORD_MSG_LOC = ("xpath", "//div[text() = 'You hovered over the Contrary']")
    NUMBER_LOC = ("xpath", "//a[text()= '1.10.32']")
    NUMBER_MSG_LOC = ("xpath", "//div[text()= 'You hovered over the 1.10.32']")
