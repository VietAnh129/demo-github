from behave import *
from page_object.nhan_su_page.nhan_su_page import NhanSu
from page_object.login_page.login_page import LoginPage
from hamcrest import assert_that, equal_to
from behave.runner import Context


@given('Login success with user "{user}" and pwd "{pwd}"')
def login_success(context: Context, user: str, pwd: str) -> None:
    LoginPage(context.driver).open_page()
    LoginPage(context.driver).input_username(user)
    LoginPage(context.driver).input_password(pwd)
    LoginPage(context.driver).click_login_button()


@when('Click Nhan su field')
def click_nhan_su(context: Context) -> None:
    NhanSu(context.driver).click_nhan_su_field()


@when('Click Ho so nhan su field')
def click_ho_so_nhan_su(context: Context) -> None:
    NhanSu(context.driver).click_ho_so_nhan_su_field()


@when('Click Nhan vien moi')
def click_nhan_vien_moi(context: Context) -> None:
    NhanSu(context.driver).click_them_moi_button()


@then('Verify auto fill UserID "{id}"')
def verify_auto_fill(context, id: str) -> None:
    assert_that(NhanSu(context.driver).verify_userid(), equal_to(id))


@when('input "{name}" in Họ và Tên field')
def input_name(context: Context, name: str) -> None:
    NhanSu(context.driver).input_name(name)


@then('verify auto capitalize first letter "{name}"')
def verify_auto_capitalize(context: Context, name: str) -> None:
    assert_that(NhanSu(context.driver).verify_auto_capitalize(), equal_to(name))


@when('click Giới tính field')
def click_gioi_tinh_field(context: Context) -> None:
    NhanSu(context.driver).click_gioi_tinh_field()


@then('verify drop list Gioi Tinh "{check_list}"')
def verify_checklist_gioi_tinh(context: Context, check_list: str) -> None:
    assert_that(NhanSu(context.driver).verify_checklist_gender(), equal_to(check_list))


@when(u'click Hoc Van field')
def click_hoc_van_field(context: Context) -> None:
    NhanSu(context.driver).click_checklist_literacy()


@then(u'verify drop list Hoc Van "{literacy}"')
def verify_hoc_van_field(context: Context, literacy: str) -> None:
    assert_that(NhanSu(context.driver).verify_checklist_literacy(), equal_to(literacy))

