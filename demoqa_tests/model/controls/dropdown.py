from selene import have
from selene.support.shared import browser


class DropDownPicker:
    def __init__(self, element):
        self.element = element

    def select(self, option):
        self.element.click()
        browser.all('[id^=react-select][id*=-option-]').by(
            have.exact_text(option)
        ).click()

    def select_by_typing(self, option):
        self.element.type(option).press_enter()
