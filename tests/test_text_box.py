import os

from selene.support.shared import browser
from selene import have


def test_submit_practice_form():
    browser.config.base_url = 'https://demoqa.com'

    browser.open('/automation-practice-form')
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(have.text('Practice Form'))

    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Smith')
    browser.element('#userEmail').type('example@ex.com')
    browser.element('.custom-control.custom-radio.custom-control-inline').click()
    browser.element('#userNumber').type('7911325783')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="1"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="2004"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--004').click()

    subject_input = browser.element('#subjectsInput')
    subject_input.type('M').press_enter()
    subject_input.type('E').press_enter()

    browser.element('.custom-control.custom-checkbox.custom-control-inline').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../blue.jpg'))
    browser.element('#currentAddress').type("Mr John Smith\n"
                                            "132, My Street,\n"
                                            "Kingston, New York 12401\n"
                                            "United States\n")

    browser.element('#react-select-3-input').type('N').press_enter()
    browser.element('#react-select-4-input').type('G').press_enter()
    browser.element('#submit').press_enter()

    browser.element('.modal-body').all('tbody tr').should(have.texts(
        'John Smith',
        'example@ex.com',
        'Male',
        '7911325783',
        '04 February,2004',
        'Maths, English',
        'Sports',
        'blue.jpg',
        'Mr John Smith 132, My Street, Kingston, New York 12401 United States',
        'NCR Gurgaon'
    ))














#    browser.element('#submit').click()
