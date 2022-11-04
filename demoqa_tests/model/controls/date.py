from selene.support.shared import browser

import selene
from selenium.webdriver.common.keys import Keys

import sys


class DatePicker:
    def __init__(self, element):
        self.element = element #newbrowser.browser.element('#dateOfBirthInput')

    def date_picker(self, month, year, day):
        self.element.click()
        print(self.element)
        self.element.element('.react-datepicker__month-select').send_keys(month)
        self.element.element('.react-datepicker__year-select').send_keys(year)
        self.element.element(
            f'.react-datepicker__day--0{day}'
            f':not(.react-datepicker__day--outside-month)'
        ).click()

# class DatePicker:
#    def __init__(self):
#        element = ...
#
#    def set_date(self, date):
#        modifyer_key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
#        self.element.send_keys(
#            modifyer_key + 'a' + Keys.NULL,
#            user.format_input_date(date),
#        ).press_enter()
#
