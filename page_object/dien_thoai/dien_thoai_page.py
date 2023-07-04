from base_page.base_page import BasePage
from selenium.webdriver.common.keys import Keys
PHONE_NUMBER_FIELD = 'phonenumber'
ERROR_PHONE = '//p[@id="phonenumber-error"]'


class DienThoai(BasePage):
    def input_phone_number_field(self, phone: str, timeout: int = 20) -> None:
        self.driver.f(PHONE_NUMBER_FIELD, timeout).send_keys(phone)

    def error_phone_number_is_displayed(self, timeout: int = 20) -> bool:
        return self.driver.is_element_displayed(ERROR_PHONE, timeout)

    def verify_error_phone_number(self, timeout: int = 20) -> str:
        error = self.driver.f(ERROR_PHONE, timeout)
        error = error.text
        return error

    def click_tab(self, timeout: int = 20) -> None:
        self.driver.f(PHONE_NUMBER_FIELD, timeout).send_keys(Keys.TAB)

    def input_space(self, timeout: int = 20) -> None:
        self.driver.f(PHONE_NUMBER_FIELD, timeout).send_keys(Keys.SPACE)
