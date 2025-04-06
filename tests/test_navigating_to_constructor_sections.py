from locators import Locators
from data import TestLinks
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestConstructorSections:

    # Проверяем вкладку "Булки"
    def test_navigating_to_buns_successful(self, driver):
        # Переходим на главную страницу
        driver.get(TestLinks.URL)

        # Нажимаем на вкладку "Начинки", чтобы уйти с вкладки по умолчанию ("Булки")
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.CONSTRUCTOR_SAUCES)
        ).click()

        # Нажимаем на вкладку "Булки"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.CONSTRUCTOR_BUNS)
        ).click()

        # Проверяем, что вкладка "Булки" теперь активна
        active_tab = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_BUNS_ACTIVE)
        )
        assert active_tab.text == "Булки"

        # Проверяем вкладку "Соусы"
    def test_navigating_to_sauces_successful(self, driver):
        # Переходим на главную страницу
        driver.get(TestLinks.URL)

        # Нажимаем на вкладку "Соусы"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.CONSTRUCTOR_SAUCES)
        ).click()

        # Проверяем, что вкладка "Соусы" теперь активна
        active_tab = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_SAUCES_ACTIVE)
        )
        assert active_tab.text == "Соусы"

    # Проверяем вкладку "Начинки"
    def test_navigating_to_fillings_successful(self, driver):
        # Переходим на главную страницу
        driver.get(TestLinks.URL)

        # Нажимаем на вкладку "Начинки"
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.CONSTRUCTOR_FILLINGS)
        ).click()

        # Проверяем, что вкладка "Соусы" теперь активна
        active_tab = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS_ACTIVE)
        )
        assert active_tab.text == "Начинки"



