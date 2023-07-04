from behave import *
from page_object.dien_thoai.dien_thoai_page import DienThoai
from hamcrest import assert_that, equal_to


@when("input phone number '{phone}' in phone number field")
def input_phone_number(context, phone):
    DienThoai(context.driver).input_phone_number_field(phone)


@when('click Tab')
def click_tab(context):
    DienThoai(context.driver).click_tab()


@then('verify error "{error_mes}" is displayed')
def verify_error_phone_number(context, error_mes):
    assert_that(DienThoai(context.driver).error_phone_number_is_displayed(), equal_to(True))
    assert_that(DienThoai(context.driver).verify_error_phone_number(), equal_to(error_mes))


@when('input Space in phone number field')
def input_space(context):
    DienThoai(context.driver).input_space()
