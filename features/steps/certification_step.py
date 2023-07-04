import time

from behave import *
from page_object.cerification.certification_page import Certification
from hamcrest import assert_that, equal_to


@when(u'go to page 10')
def go_to_page_10(context):
    Certification(context.driver).go_to_page_10()


@when(u'click user Le Nam')
def click_user(context):
    Certification(context.driver).click_user()


@when(u'click Certification field')
def click_cer_field(context):
    Certification(context.driver).click_cer_field()


@then(u'click Add new button')
def click_add_new_button(context):
    Certification(context.driver).click_add_new_button()


@when(u'fill all parameters in Them moi field')
def fill_all_para(context):
    Certification(context.driver).fill_all_para()


@when(u'click Luu button')
def click_save_button(context):
    Certification(context.driver).click_luu_button()


@when(u'verify popup successful is displayed')
def verify_popup(context):
    assert_that(Certification(context.driver).verify_popup_is_displayed,equal_to(True))


@step(u'go back to Dao Tao page')
def go_back_page(context):
    assert_that(Certification(context.driver).verify_go_back_page(), equal_to(True))


@then(u'verify all parameters is displayed')
def verify_all_para(context):
    assert_that(Certification(context.driver).verify_all_para_is_displayed(), equal_to(True))
