import os

from selenium_test.page_object.address_book import addressBook
from selenium_test.page_object.base_page import *


class improtAddressBook(basePage):
    # 通讯录导入通讯录页面元素
    _import_addressBook_file = (By.CSS_SELECTOR,'#js_upload_file_input')
    # 定义导入通讯录提交元素
    _import_addressBook_sumbit = (By.CSS_SELECTOR, '[id=submit_csv]')

    #导入通讯录
    def import_addressBook(self,filename="../file/address.xlsx"):
        #获取导入文件的绝对路径
        filepath=os.path.dirname(__file__)
        filename=os.path.abspath(os.path.join(filepath,filename))

        #上传通讯录文件
        self.find(*self._import_addressBook_file).send_keys(filename)
        #点击提交
        self.find(*self._import_addressBook_sumbit).click()
        return addressBook(self._driver)