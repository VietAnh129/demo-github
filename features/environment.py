from core.custom_web_driver import CustomWebDriver


def before_scenario(context, scenario):
    context.driver = CustomWebDriver()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.close()
