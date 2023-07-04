from base_page.base_page import BasePage

NHAN_SU_FIELD = '//span[@class="menu-text"and contains(text(),"Nhân sự")]'
HO_SO_NHAN_SU_FIELD = '//span[@class="sub-menu-text"and contains(text(),"Hồ sơ nhân sự")]'
THEM_MOI_BUTTON = '//a[@class="btn mright5 btn-info pull-left display-block hidden-xs"]'
USERID = 'staff_identifi'
NAME_FIELD = 'firstname'
GENDER_FIELD = '//div[@class="filter-option-inner-inner" and contains(text(),"Nam")]'
GENDER_CHECKLIST = '//select[@id="sex"]//option'
LITERACY_FIELD = '//button[@data-id="literacy"]'
LITERACY_CHECKLIST = '//select[@id="literacy"]//option'


class NhanSu(BasePage):

    def click_nhan_su_field(self, timeout: int = 20) -> None:
        self.driver.f(NHAN_SU_FIELD, timeout).click()

    def click_ho_so_nhan_su_field(self, timeout: int = 20) -> None:
        self.driver.wait_for_element_displayed(HO_SO_NHAN_SU_FIELD, timeout)
        self.driver.f(HO_SO_NHAN_SU_FIELD, timeout).click()

    def click_them_moi_button(self, timeout: int = 20) -> None:
        self.driver.f(THEM_MOI_BUTTON, timeout).click()

    def verify_userid(self, timeout: int = 20) -> None:
        userIDx = self.driver.f(USERID, timeout)
        userID = userIDx.get_attribute('value')
        return userID

    def input_name(self,  name: str, timeout: int = 20) -> None:
        self.driver.f(NAME_FIELD, timeout).send_keys(name)

    def verify_auto_capitalize(self, timeout: int = 20) -> str:
        namex = self.driver.f(NAME_FIELD, timeout)
        name = namex.get_attribute('value')
        return name

    def click_gioi_tinh_field(self, timeout: int = 20) -> None:
        self.driver.f(GENDER_FIELD, timeout).click()

    def verify_checklist_gender(self, timeout: int = 20, ):
        list = ''
        elements = self.driver.fa(GENDER_CHECKLIST)
        for i in elements:
            element = i.text + ','
            list += element
        list_gender = list.strip(',')
        return list_gender

    def click_checklist_literacy(self, timeout: int = 20, ):
        self.driver.f(LITERACY_FIELD, timeout).click()

    def verify_checklist_literacy(self, timeout: int = 20, ):
        list = ''
        elements = self.driver.fa(LITERACY_CHECKLIST, timeout)
        for i in elements:
            element = i.text + ','
            list += element
        list_literacy = list.strip(',')
        return list_literacy

