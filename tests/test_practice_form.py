from time import sleep

from demoqa_tests.model import app
from demoqa_tests.model.pages.registration_form import NewBrowser
from tests.test_data.users import yuri
from demoqa_tests.utils import attach


def test_submit_student_nb(setup_browser):
    nb = NewBrowser(setup_browser)
    nb.given_opened()

    # WHEN
    nb.set_field('#firstName', yuri.name)
    nb.set_field('#lastName', yuri.last_name)
    nb.set_field('#userEmail', yuri.email)

    nb.set_gender(yuri.gender.value)

    '''
    # OR
    gender_male = browser.element('[for=gender-radio-1]')
    gender_male.click()
    # OR
    browser.element('[id^=gender-radio][value=Male]').perform(command.js.click)
    browser.element('[id^=gender-radio][value=Male]').element(
        './following-sibling::*'
    ).click()
    # OR better:
    browser.element('[id^=gender-radio][value=Male]').element('..').click()
    # OR
    browser.all('[id^=gender-radio]').element_by(have.value('Male')).element('..').click()
    browser.all('[id^=gender-radio]').by(have.value('Male')).first.element('..').click()
    '''

    nb.set_field('#userNumber', yuri.user_number)

    nb.set_date(yuri.birth_month, yuri.birth_year, yuri.birth_day)
    '''
    # OR something like
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('28 Mar 1995').press_enter()
    '''

    nb.add_subjects(yuri.subjects)

    nb.set_hobbies(yuri.hobbies)

    nb.send_file(yuri.picture_file)

    nb.set_field('#currentAddress', yuri.current_address)

    nb.scroll_to_bottom()

    nb.set_state_by_typing(yuri.state)
    nb.set_city_by_typing(yuri.city)
    sleep(5)
    nb.submit()

    # THEN

    nb.should_have_submitted(
        [
            ('Student Name', f'{yuri.name} {yuri.last_name}'),
            ('Student Email', yuri.email),
            ('Gender', yuri.gender.value),
            ('Mobile', yuri.user_number),
            ('Date of Birth', f'{yuri.birth_day} {yuri.birth_month},{yuri.birth_year}'),
            ('Subjects', 'History'),
            ('Hobbies', 'Sports'),
            ('Picture', yuri.picture_file),
            ('Address', yuri.current_address),
            ('State and City', f'{yuri.state} {yuri.city}'),
        ],
    )

#    browser.element('#submit').click()
