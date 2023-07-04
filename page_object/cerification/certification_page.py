import time

from base_page.base_page import BasePage
_PAGE_10 = '//li[@class="paginate_button "]//a[@data-dt-idx="7"]'
_LE_NAM_USER = '//a[contains(text(),"LÊ ĐÌNH  HẢI")]'
_CER_BUTTON = '//i[@class="fa fa-certificate"]'
_ADD_NEW_BUTTON = '//button[@onclick="add_certificate();"]'
_TYPE_BUTTON = '//button[@data-id="doctype"]'
_TYPE_CER = '//a[@id="bs-select-4-2"]//span[contains(text(), "CSWIP 3.1")]'
_NGAY_CAP_FIELD = '//div[@app-field-wrapper="year"]//input'
_NGAY_HET_HAN_FIELD = '//div[@app-field-wrapper="date_expiration"]//input'
_PLACE_FIELD = '//input[@id="address"]'
_SAVE_BUTTON = '//div[@style="text-align:right"]//button[@id="btn_save_literacy"]'
_POPUP_ADD_CER_SUCCESS = '//div[@class="float-alert animated fadeInRight col-xs-10 col-sm-3 alert alert-success"'
_UPDATE_CER = '//table[@id="DataTables_Table_1"]'
ngay_cap = '12-12-2022'
ngay_het_han = '12-12-2021'
place = 'TPHCM'


class Certification(BasePage):

    def go_to_page_10(self, timeout: int = 20) -> None:
        self.driver.f(_PAGE_10, timeout).click()

    def click_user(self, timeout: int = 20) -> None:
        self.driver.execute_script("scroll(0, -500);")
        time.sleep(5)
        self.driver.f(_LE_NAM_USER, timeout).click()

    def click_cer_field(self, timeout: int = 20) -> None:
        self.driver.f(_CER_BUTTON, timeout).click()

    def click_add_new_button(self, timeout: int = 20) -> None:
        self.driver.f(_ADD_NEW_BUTTON, timeout).click()

    def fill_all_para(self, timeout: int = 20) -> None:
        # self.driver.f(_TYPE_BUTTON, timeout).click()
        # self.driver.f(_TYPE_CER, timeout).click()
        self.driver.f(_PLACE_FIELD, timeout).send_keys(place)
        self.driver.f(_NGAY_CAP_FIELD, timeout).send_keys(ngay_cap)
        self.driver.f(_NGAY_HET_HAN_FIELD, timeout).send_keys(ngay_het_han)

    def click_luu_button(self, timeout: int = 20) -> None:
        self.driver.f(_SAVE_BUTTON, timeout).click()

    def verify_popup_is_displayed(self, timeout: int = 20) -> bool:
        return self.driver.is_element_displayed(_POPUP_ADD_CER_SUCCESS, timeout)

    def verify_go_back_page(self, timeout: int = 20) -> bool:
        return self.driver.is_element_displayed(_CER_BUTTON, timeout)

    def verify_all_para_is_displayed(self, timeout: int = 20) -> bool:
        return self.driver.is_element_displayed(_UPDATE_CER, timeout)




