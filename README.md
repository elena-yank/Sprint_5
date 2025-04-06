#  Sprint_5

## Автотесты для Stellar Burgers

### test_registration.py
test_valid_password_lengths_successful — пользовать успешно зарегистрирован с паролями валидной длины, ГЗ: 6, 7; КЭ: 10

test_short_passwords_unsuccessful — пользователь не может зарегистрироваться со слишком короткими паролями, ГЗ: 5, КЭ: 3

### test_login.py
test_login_on_main_page_successful — пользователь успешно логинится с главной страницы

test_account_login_on_main_page_successful — пользователь успешно логинится через личный кабинет

test_login_on_registration_page_successful — пользователь успешно логинится при нажатии на кнопку "Войти" на странице регистрации аккаунта

test_login_on_forgot_password_page_successful — пользователь успешно логинится со страницы восстановления пароля

### test_logout.py

test_logout_successful — пользователь успешно выходит из аккаунта при нажатии на кнопку "Выход" в личном кабинете

### test_navigating_to_account.py

test_open_account_info_successful — залогиненный пользователь успешно заходит в личный кабинет

P.S.: То, что незалогиненный пользователь при нажатии на кнопку "Личный кабинет" попадает на страницу входа в аккаунт, протестировано в файле test_login.py, тест test_account_login_on_main_page_successful  

### test_navigating_to_constructor.py

test_navigating_to_constructor_successful — пользователь успешно переходит в конструктор из личного кабинета при нажатии на "Конструктор"

test_navigating_to_constructor_from_logo_successful — пользователь успешно переходит в конструктор из личного кабинета при нажатии на логотип Stellar Burgers

### test_navigating_to_constructor_sections.py

test_navigating_to_buns_successful — пользователь успешно переключается на раздел "Булки"

test_navigating_to_sauces_successful — пользователь успешно переключается на раздел "Соусы"

test_navigating_to_fillings_successful — пользователь успешно переключается на раздел "Начинки"