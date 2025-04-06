from locators import Locators
from data import MyUser, TestLinks
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogout:

    # Выход из аккаунта. Не забываем сначала в него залогиниться.
    def test_logout_successful(self, driver):
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

        # Нажимаем на кнопку "Личный кабинет"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_LINK_PERSONAL_ACCOUNT)
        ).click()

        # Ждём, пока загрузится Личный кабинет
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(TestLinks.ACCOUNT_PAGE)
        )

        # Нажимаем на кнопку "Выход"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        ).click()

        # Ждём, пока загрузится страница входа в аккаунт
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(TestLinks.LOGIN_PAGE)
        )

        # Проверяем, что активная ссылка совпадает с адресом страницы входа в аккаунт
        assert driver.current_url == TestLinks.LOGIN_PAGE