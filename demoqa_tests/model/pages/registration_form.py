from typing import Tuple

from selene import have, command

from selene.support.shared.jquery_style import ss

from demoqa_tests.model.controls import dropdown, modal, date
from tests.test_data.users import Subject
from demoqa_tests.utils import path
import allure
from allure_commons.types import Severity


class NewBrowser:
    def __init__(self, browser):
        self.browser = browser

    def given_opened(self):
        self.browser.open("https://demoqa.com/automation-practice-form")
        self.browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        self.browser.driver.execute_script("$('footer').remove()")
        self.browser.driver.execute_script("$('#fixedban').remove()")

    @allure.step("Добавить предметы {values}")
    def add_subjects(self, values: Tuple[Subject]):
        for subject in values:
            self.browser.element('#subjectsInput').type(subject.value).press_enter()

    @allure.step("Установить город {value}")
    def set_state(self, value: str):
        dropdown.select(self.browser.element('#state'), value)

    @allure.step("Установить страну {value}")
    def set_city(self, value: str):
        dropdown.select(self.browser.element('#city'), value)

    @allure.step("Установить страну {value}")
    def set_state_by_typing(self, value: str):
        dropdown.select_by_typing(self.browser.element('#react-select-3-input'), value)

    @allure.step("Установить город {value}")
    def set_city_by_typing(self, value: str):
        dropdown.select_by_typing(self.browser.element('#react-select-4-input'), value)

    @allure.step("Промотать вниз")
    def scroll_to_bottom(self):
        self.browser.element('#state').perform(command.js.scroll_into_view)

    @allure.step("Проверка данных")
    def should_have_submitted(self, data):
        rows = self.browser.element('.modal-content').all('tbody tr')
        for row, value in data:
            rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))

    @allure.step("Установить {selector} в значение {text}")
    def set_field(self, selector, text):
        self.browser.element(selector).type(text)

    @allure.step("Установить значение gender в {gender}")
    def set_gender(self, gender):
        self.browser.all('[for^=gender-radio]').by(have.exact_text(gender)).first.click()

    @allure.step("Установить дату  в {day}-{month}-{year}")
    def set_date(self, month, year, day):
        date.date_picker(month, year, day, self)

    @allure.step("Отправить файл {file}")
    def send_file(self, file):
        self.browser.element('[id="uploadPicture"]').send_keys(
            path.to_resource(file)
        )

    @allure.step("Установить hobbies {hobbies}")
    def set_hobbies(self, hobbies):
        for hobby in hobbies:
            self.browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element('..').click()

    @allure.step("Нажать отправить")
    def submit(self):
        self.browser.element('#submit').perform(command.js.click)
