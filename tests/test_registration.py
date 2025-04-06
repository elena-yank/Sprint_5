import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import TestUser, TestLinks

# Регистрация с паролями валидной длины, ГЗ: 6, 7; КЭ: 10
class TestSuccessfulRegistration:

    @pytest.mark.parametrize("password_length", [6, 7, 10])
    def test_valid_password_lengths_successful(self, driver, password_length):

        driver.get(TestLinks.REGISTRATION_PAGE)
        user = TestUser.generate_user(password_length=password_length)

        # Заполнение формы
        driver.find_element(*Locators.NAME_FIELD).send_keys(user['name'])
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(user['email'])
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(user['password'])
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # Ждём, пока загрузится страница входа
        WebDriverWait(driver, 10).until(
            EC.url_to_be(TestLinks.LOGIN_PAGE)
        )

        # Удостоверяемся, что активная страница совпадает с адресом страницы входа
        assert driver.current_url == TestLinks.LOGIN_PAGE

# Регистрация с паролями невалидной длины, ГЗ: 5, КЭ: 3
class TestInvalidPasswords:

    @pytest.mark.parametrize("password_length", [3, 5])
    def test_short_passwords_unsuccessful(self, driver, password_length):

        driver.get(TestLinks.REGISTRATION_PAGE)
        user = TestUser.generate_user(password_length=password_length)

        driver.find_element(*Locators.NAME_FIELD).send_keys(user['name'])
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(user['email'])
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(user['password'])
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # Проверяем сообщение об ошибке
        assert driver.find_element(*Locators.PASSWORD_ERROR).text == "Некорректный пароль"

        # Проверяем, что активной страницей осталась страница регистрации
        assert driver.current_url == TestLinks.REGISTRATION_PAGE