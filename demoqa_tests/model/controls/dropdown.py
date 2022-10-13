from selene import have
from selene.support.shared import browser


def select(element, option):
    element.click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(option)
    ).click()


def select_by_typing(element, option):
    element.type(option).press_enter()


