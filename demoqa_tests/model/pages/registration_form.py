from typing import Tuple

from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss

from demoqa_tests.model.controls import dropdown, modal, date
from tests.test_data.users import Subject
from demoqa_tests.utils import path

state = browser.element('#state')


def given_opened():
    browser.open('/automation-practice-form')
    ads = ss('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=10).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def set_state(value: str):
    dropdown.select(state, value)


def set_city(value: str):
    dropdown.select(browser.element('#city'), value)


def set_state_by_typing(value: str):
    dropdown.select_by_typing(browser.element('#react-select-3-input'), value)


def set_city_by_typing(value: str):
    dropdown.select_by_typing(browser.element('#react-select-4-input'), value)

def scroll_to_bottom():
    state.perform(command.js.scroll_into_view)


def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))


def set_field(selector, text):
    browser.element(selector).type(text)


def set_gender(gender):
    browser.all('[for^=gender-radio]').by(have.exact_text(gender)).first.click()


def set_date(month, year, day):
    date.date_picker(month, year, day)


def send_file(file):
    browser.element('[id="uploadPicture"]').send_keys(
        path.to_resource(file)
    )


def set_hobbies(hobbies):
    for hobby in hobbies:
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element('..').click()


def submit():
    browser.element('#submit').perform(command.js.click)
