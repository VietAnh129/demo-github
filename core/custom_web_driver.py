from core.custom_web_selector import WebSelector
from selenium.webdriver.remote.webelement import WebElement
from typing import Any, Optional
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from typing import List
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, TimeoutException)


class CustomWebDriver(webdriver.Chrome):

    def f(self, selector: str, timeout: int = 20, **kwargs: Optional[Any]) -> WebElement:
        by, value = WebSelector(selector, **kwargs).get_locator()
        try:
            return WebDriverWait(
                self, timeout, ignored_exceptions=ignored_exceptions).until(ec.presence_of_element_located((by, value)))

        except TimeoutException as e:
            print(f'Could not found element with {by},{value}')
            raise e

    def fa(self, selector: str, timeout: int = 20, **kwargs: Optional[Any]) -> List[WebElement]:
        by, value = WebSelector(selector, **kwargs).get_locator()
        try:
            return WebDriverWait(self, timeout).until(ec.presence_of_all_elements_located((by, value)))
        except TimeoutException:
            print(f'Could not found element with {by},{value}')

    def wait_for_element_displayed(self, selector: str, timeout: int = 20, **kwargs: Optional[Any]) -> WebElement:
        by, value = WebSelector(selector, **kwargs).get_locator()
        return WebDriverWait(self, timeout).until(ec.visibility_of_element_located((by, value)))

    def is_element_displayed(self, selector: str, timeout: int = 20, **kwargs: Optional[Any]) -> bool:
        by, value = WebSelector(selector, **kwargs).get_locator()
        try:
            element = self.f(selector, timeout, **kwargs)
            element.is_displayed()
            return True
        except TimeoutException:
            print('The element is not displayed')
            return False

    def get_text_from_selector(self, selector: str) -> str:
        return self.f(selector).text








