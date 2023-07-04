from base_page.base_page import BasePage
from selenium import webdriver
from core.custom_web_driver import CustomWebDriver
url = "https://alpha.digityze.asia/authentication/login"
USERNAME_FIELD = 'email'
PASSWORD_FIELD = 'password'
LOGIN_BUTTON = '//button[@class="btn btn-primary btn-block"]'
VERIFY_LOGIN_SUCCESS = '//span[contains(text(),"Bảng tin")]'
ERROR_MESS_LOGIN = '//div[@class="text-center alert alert-danger"]'


class LoginPage(BasePage):
    def open_page(self):
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get(url)

    def input_username(self, user: str, timeout: int = 10) -> None:
        self.driver.f(USERNAME_FIELD, timeout).send_keys(user)

    def input_password(self, pwd: str, timeout: int = 10) -> None:
        self.driver.f(PASSWORD_FIELD, timeout).send_keys(pwd)

    def click_login_button(self, timeout: int = 10) -> None:
        self.driver.f(LOGIN_BUTTON, timeout).click()

    def verify_login_successfully(self) -> str:
        title = self.driver.title
        return title

    def verify_error_mess(self, timeout: int = 10) -> str:
        error_mess = self.driver.f(ERROR_MESS_LOGIN, timeout).text
        return error_mess
