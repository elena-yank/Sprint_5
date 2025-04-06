import random
import string

# Генерируем пользователя с указанной длиной пароля
class TestUser:
    @staticmethod
    def generate_user(password_length=6):
        random_numbers = ''.join(random.choices(string.digits, k=4))

        return {
            'name': f"NewUser{random_numbers}",
            'email': f"TestEmail{random_numbers}@yandex.ru",
            'password': ''.join(random.choices(string.digits, k=password_length))
        }

class MyUser:
    MY_USER_EMAIL = "elenaiankovskaia17666@yandex.ru"
    MY_USER_PASSWORD = "AhAPSF22"

class TestLinks:
    URL = "https://stellarburgers.nomoreparties.site/"
    LOGIN_PAGE = URL + "login"
    REGISTRATION_PAGE = URL + "register"
    ACCOUNT_PAGE = URL + "account/profile"
    FORGOT_PASSWORD_PAGE = URL + "forgot-password"