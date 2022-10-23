from time import sleep

from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model import app
from demoqa_tests.model.pages import registration_form
from demoqa_tests.model.pages.registration_form import (
    given_opened,
)
from demoqa_tests.utils import path
from tests.test_data.users import yuri


def test_fail_to_submit_form():
    given_opened()

    # todo: implement


def test_submit_student_registration_form():

    app.registration_form.given_opened()

    # WHEN
    registration_form.set_field('#firstName', yuri.name)
    registration_form.set_field('#lastName', yuri.last_name)
    registration_form.set_field('#userEmail', yuri.email)

    registration_form.set_gender(yuri.gender.value)

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

    registration_form.set_field('#userNumber', yuri.user_number)

    registration_form.set_date(yuri.birth_month, yuri.birth_year, yuri.birth_day)
    '''
    # OR something like
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('28 Mar 1995').press_enter()
    '''

    registration_form.add_subjects(yuri.subjects)

    registration_form.set_hobbies(yuri.hobbies)

    registration_form.send_file(yuri.picture_file)

    registration_form.set_field('#currentAddress', yuri.current_address)

    registration_form.scroll_to_bottom()

    registration_form.set_state_by_typing(yuri.state)
    registration_form.set_city_by_typing(yuri.city)
    sleep(5)
    registration_form.submit()

    # THEN

    registration_form.should_have_submitted(
        [
            ('Student Name', f'{yuri.name} {yuri.last_name}'),
            ('Student Email', yuri.email),
            ('Gender', yuri.gender.value),
        ],
    )













#    browser.element('#submit').click()
