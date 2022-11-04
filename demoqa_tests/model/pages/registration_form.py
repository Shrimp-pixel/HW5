from typing import Tuple
from time import sleep

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
        self.date_of_birth_picker = date.DatePicker(browser.element('#dateOfBirth'))
        self.dropdown_city = dropdown.DropDownPicker(browser.element('#state'))
        self.dropdown_state = dropdown.DropDownPicker(browser.element('#city'))

        self.dropdown_city_by_typing = dropdown.DropDownPicker(browser.element('#react-select-3-input'))
        self.dropdown_state_by_typing = dropdown.DropDownPicker(browser.element('#react-select-4-input'))

    def given_opened(self):
        self.browser.open("https://demoqa.com/automation-practice-form")
        self.browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        self.browser.driver.execute_script("$('footer').remove()")
        self.browser.driver.execute_script("$('#fixedban').remove()")
        return self

    @allure.step("Добавить предметы {values}")
    def add_subjects(self, values: Tuple[Subject]):
        for subject in values:
            self.browser.element('#subjectsInput').type(subject.value).press_enter()
        return self

    @allure.step("Установить город {value}")
    def set_state(self, value: str):
        self.dropdown_city.select(value)
        return self

    @allure.step("Установить страну {value}")
    def set_city(self, value: str):
        self.dropdown_state.select(value)
        return self

    @allure.step("Установить страну {value}")
    def set_state_by_typing(self, value: str):
        self.dropdown_city_by_typing.select_by_typing(value)
        return self

    @allure.step("Установить город {value}")
    def set_city_by_typing(self, value: str):
        self.dropdown_state_by_typing.select_by_typing(value)
        return self

    @allure.step("Промотать вниз")
    def scroll_to_bottom(self):
        self.dropdown_city.element.perform(command.js.scroll_into_view)
        return self

    @allure.step("Проверка данных")
    def should_have_submitted(self, data):
        rows = self.browser.element('.modal-content').all('tbody tr')
        for row, value in data:
            rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
        return self

    @allure.step("Установить {selector} в значение {text}")
    def set_field(self, selector, text):
        self.browser.element(selector).type(text)
        return self

    @allure.step("Установить значение gender в {gender}")
    def set_gender(self, gender):
        self.browser.all('[for^=gender-radio]').by(have.exact_text(gender)).first.click()
        return self

    @allure.step("Установить дату  в {day}-{month}-{year}")
    def set_date(self, month, year, day):
        self.date_of_birth_picker.date_picker(month, year, day)
        return self

    @allure.step("Отправить файл {file}")
    def send_file(self, file):
        self.browser.element('[id="uploadPicture"]').send_keys(
            path.to_resource(file)
        )
        return self

    @allure.step("Установить hobbies {hobbies}")
    def set_hobbies(self, hobbies):
        for hobby in hobbies:
            self.browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element('..').click()

        return self

    @allure.step("Нажать отправить")
    def submit(self):
        self.browser.element('#submit').perform(command.js.click)
        return self

    @allure.step('Заполнить форму')
    def fill_form(self, user):
        self.set_field('#firstName', user.name)
        self.set_field('#lastName', user.last_name)
        self.set_field('#userEmail', user.email)

        self.set_gender(user.gender.value)

        self.set_field('#userNumber', user.user_number)

        self.set_date(user.birth_month, user.birth_year, user.birth_day)

        self.add_subjects(user.subjects)

        self.set_hobbies(user.hobbies)

        self.send_file(user.picture_file)

        self.set_field('#currentAddress', user.current_address)

        self.scroll_to_bottom()

        self.set_state_by_typing(user.state)
        self.set_city_by_typing(user.city)
        sleep(5)
        return self
