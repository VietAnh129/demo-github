from behave import *
from hamcrest import assert_that, equal_to
from page_object.login_page.login_page import LoginPage


@given('Open page')
def open_page(context):
    LoginPage(context.driver).open_page()


@when('Input username "{user}" and password "{pwd}"')
def input_user_and_pwd(context, user, pwd):
    LoginPage(context.driver).input_username(user)
    LoginPage(context.driver).input_password(pwd)


@when('Click login button')
def click_login_button(context):
    LoginPage(context.driver).click_login_button()


@then('Verify login successfully title "{title}"')
def verify_login_successful(context, title):
    assert_that(LoginPage(context.driver).verify_login_successfully(), equal_to(title))


@then('Verify error message "{error_mess}"')
def verify_error_mess_login(context, error_mess):
    assert_that(LoginPage(context.driver).verify_error_mess(), equal_to(error_mess))
