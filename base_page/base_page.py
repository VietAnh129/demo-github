from typing import Optional
from behave.runner import Context
from core.custom_web_driver import CustomWebDriver


class BasePage:
    myWeb: CustomWebDriver
    platform: str

    def __init__(self, driver: Optional[CustomWebDriver] = None) -> None:
        self.driver = driver

