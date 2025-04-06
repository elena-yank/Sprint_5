from locators import Locators
from data import MyUser, TestLinks
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:

    # Вход с главной страницы
    def test_login_on_main_page_successful(self, driver):
        # Переходим на главную страницу
        driver.get(TestLinks.URL)

        # Нажимаем на кнопку "Войти в аккаунт"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ).click()

        # Вводим Email
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_EMAIL)
        ).send_keys(MyUser.MY_USER_EMAIL)

        # Вводим пароль
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(MyUser.MY_USER_PASSWORD)

        # Нажимаем на кнопку "Войти"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON_LOGIN_PAGE)
        ).click()

        # Ждём, пока загрузится главная страница
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(TestLinks.URL)
        )

        # Проверяем, что активная ссылка совпадает с адресом главной страницы
        assert driver.current_url == TestLinks.URL

    # Вход через Личный кабинет на главной странице
    def test_account_login_on_main_page_successful(self, driver):

        # Переходим на главную страницу
        driver.get(TestLinks.URL)

        # Нажимаем на кнопку "Личный кабинет"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_LINK_PERSONAL_ACCOUNT)
        ).click()

        # Вводим Email
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_EMAIL)
        ).send_keys(MyUser.MY_USER_EMAIL)

        # Вводим пароль
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(MyUser.MY_USER_PASSWORD)

        # Нажимаем на кнопку "Войти"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON_LOGIN_PAGE)
        ).click()

        # Ждём, пока загрузится главная страница
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(TestLinks.URL)
        )

        # Проверяем, что активная ссылка совпадает с адресом главной страницы
        assert driver.current_url == TestLinks.URL

    # Вход через страницу Регистрации
    def test_login_on_registration_page_successful(self, driver):

        # Переходим на страницу Регистрации
        driver.get(TestLinks.REGISTRATION_PAGE)

        # Нажимаем на кнопку "Войти"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON_REGISTRATION_PAGE)
        ).click()

        # Вводим Email
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_EMAIL)
        ).send_keys(MyUser.MY_USER_EMAIL)

        # Вводим пароль
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(MyUser.MY_USER_PASSWORD)

        # Нажимаем на кнопку "Войти"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON_LOGIN_PAGE)
        ).click()

        # Ждём, пока загрузится главная страница
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(TestLinks.URL)
        )

        # Проверяем, что активная ссылка совпадает с адресом главной страницы
        assert driver.current_url == TestLinks.URL

    # Вход через страницу Восстановление пароля
    def test_login_on_forgot_password_page_successful(self, driver):

        # Переходим на страницу Восстановление пароля
        driver.get(TestLinks.FORGOT_PASSWORD_PAGE)

        # Нажимаем на кнопку "Войти"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON_FORGOT_PASSWORD_PAGE)
        ).click()

        # Вводим Email
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_EMAIL)
        ).send_keys(MyUser.MY_USER_EMAIL)

        # Вводим пароль
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(MyUser.MY_USER_PASSWORD)

        # Нажимаем на кнопку "Войти"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON_LOGIN_PAGE)
        ).click()

        # Ждём, пока загрузится главная страница
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(TestLinks.URL)
        )

        # Проверяем, что активная ссылка совпадает с адресом главной страницы
        assert driver.current_url == TestLinks.URL