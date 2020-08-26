import shelve

from selenium_test.page_object.add_member import addMember
from selenium_test.page_object.address_book import addressBook
from selenium_test.page_object.base_page import *
from selenium_test.page_object.import_addressBook import improtAddressBook


class indexPage(basePage):
    #企业微信首页地址链接
    _base_url="https://work.weixin.qq.com/wework_admin/frame#index"

    #导航:首页元素
    _index_=(By.CSS_SELECTOR,'[id="menu_index"]')

    #首页:添加成员定义元素
    _add_menber_=(By.CSS_SELECTOR,'[node-type="addmember"]')

    #首页:导入通讯录定义元素
    _import_addressBook_=(By.CSS_SELECTOR,'[node-type=import]')

    #导航：通讯录元素
    _addressBook_=(By.CSS_SELECTOR,'[id="menu_contacts"]')

    #添加cookies登录
    def add_cookies(self):
        db = shelve.open("../file/cookies")
        cookies = db['cookies']
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.get(self._base_url)

    # 首页：点击添加成员跳到添加成员页面
    def goto_add_member(self):
        self.find(*self._add_menber_).click()
        return addMember(self._driver)

    # 首页：点击导入通讯录跳到导入通讯录页面
    def goto_import_addressBook(self):
        self.find(*self._import_addressBook_).click()
        return improtAddressBook(self._driver)

    # 首页：点击导航通讯录跳到通讯录页面
    def goto_addressBook(self):
        self.find(*self._addressBook_).click()
        return addressBook(self._driver)

    # 点击导航跳回首页
    def goto_index(self):
        self.find(*self._index_).click()
        return indexPage(self._driver)
