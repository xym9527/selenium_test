import uuid

from selenium_test.page_object.base_page import *


class addMember(basePage):
    # 添加成员页面元素
    _add_menber_username = (By.CSS_SELECTOR, '[id="username"]')
    _add_menber_usernameother = (By.CSS_SELECTOR, '[id="memberAdd_english_name"]')
    _add_menber_acctid = (By.CSS_SELECTOR, '[id="memberAdd_acctid"]')
    _add_menber_gender_M = (By.XPATH, '//*[@name="gender" and @value="1"]//..')
    _add_menber_gender_F = (By.XPATH, '//*[@name="gender" and @value="2"]//..')
    _add_menber_phone = (By.CSS_SELECTOR, '[id="memberAdd_phone"]')
    _add_menber_save = (By.CSS_SELECTOR, '[class="member_colRight_operationBar ww_operationBar"]:nth-child(3) [class="qui_btn ww_btn js_btn_save"]')

    #添加成员并提交
    def add_member(self,username,phone):
        #输入姓名
        self.find(*self._add_menber_username).send_keys(username)
        #输入别名
        self.find(*self._add_menber_usernameother).send_keys("English Wang")
        #输入唯一识别码
        self.find(*self._add_menber_acctid).send_keys(str(uuid.uuid1()))
        #选择性别
        self.find(*self._add_menber_gender_M).click()
        #输入手机号
        self.find(*self._add_menber_phone).send_keys(phone)
        #获取保存按钮
        save_el=self.find(*self._add_menber_save)
        #滚动页面使保存按钮可见
        self.scrollToElement(save_el)
        #点击保存按钮
        save_el.click()

        #返回通讯录页面对象
        from selenium_test.page_object.address_book import addressBook
        return addressBook(self._driver)

