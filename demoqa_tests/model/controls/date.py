from selene.support.shared import browser


def date_picker(month, year, day, newbrowser):
    newbrowser.browser.element('#dateOfBirthInput').click()
    newbrowser.browser.element('.react-datepicker__month-select').send_keys(month)
    newbrowser.browser.element('.react-datepicker__year-select').send_keys(year)
    newbrowser.browser.element(
        f'.react-datepicker__day--0{day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()
