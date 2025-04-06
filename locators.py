from selenium.webdriver.common.by import By

class Locators:

    # Страница регистрации
    # Поле "Имя"
    NAME_FIELD = (By.XPATH, "//label[contains(text(), 'Имя')]/../input")
    # Поле "Email"
    EMAIL_FIELD = (By.XPATH, "//label[contains(text(), 'Email')]/../input")
    # Поле "Пароль"
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    # Кнопка "Зарегистрироваться"
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Ошибка пароля
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']")

    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка "Личный кабинет" на главной странице
    LOGIN_LINK_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Страница входа:
    # Поле Email на странице входа
    LOGIN_EMAIL = (By.XPATH, "//input[@type='text' and @name='name']")
    # Поле Пароль на странице входа
    LOGIN_PASSWORD = (By.XPATH, "//input[@type='password']")
    # Кнопка "Войти" на странице входа
    LOGIN_BUTTON_LOGIN_PAGE = (By.XPATH, "//button[text()='Войти']")
    # Кнопка "Зарегистрироваться" на странице входа
    REGISTRATION_BUTTON_LOGIN_PAGE = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # Кнопка "Восстановить пароль" на странице входа
    FORGOT_PASSWORD_LOGIN_PAGE = (By.XPATH, "//a[@href='/forgot-password']")

    # Кнопка "Войти" на странице Регистрации
    LOGIN_BUTTON_REGISTRATION_PAGE = (By.XPATH, "//a[text()='Войти']")
    # Кнопка "Войти" на странице Восстановление пароля
    LOGIN_BUTTON_FORGOT_PASSWORD_PAGE = (By.XPATH, "//a[text()='Войти']")

    # Кнопка "Конструктор" в Личном кабинете
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип "Stellar Burgers"
    BURGERS_LOGO = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]")

    # Кнопка "Выход" в Личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Разделы конструктора
    CONSTRUCTOR_BUNS = (By.XPATH, "//span[text()='Булки']")
    CONSTRUCTOR_SAUCES = (By.XPATH, "//span[text()='Соусы']")
    CONSTRUCTOR_FILLINGS = (By.XPATH, "//span[text()='Начинки']")

    # Активные вкладки
    CONSTRUCTOR_BUNS_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']")
    CONSTRUCTOR_SAUCES_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Соусы']")
    CONSTRUCTOR_FILLINGS_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']")




