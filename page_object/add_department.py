import uuid

from selenium_test.page_object.base_page import *


class addDepartment(basePage):

    #通讯录添加部门页面元素
    _add_department_flag='class="qui_dialog ww_dialog qui_dialog ww_dialog ww_dialog_WithInput member_tag_dialog"]'
    _add_department_name=(By.CSS_SELECTOR,'[class="qui_inputText ww_inputText"][name="name"]')
    #定义部门列表元素
    _add_department_parent=(By.CSS_SELECTOR,'[class="qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list"]')
    #定义选择归属的部门元素
    _add_department_parentSelect=(By.CSS_SELECTOR,'[class="member_tag_dialog_inputDlg"] [id="1688850762041605_anchor"]')
    _add_department_sumbit=(By.CSS_SELECTOR,'[class="qui_btn ww_btn ww_btn_Blue"]')

    #添加部门
    def add_department(self,name):
        #输入部门名称
        self.find(*self._add_department_name).send_keys(name)
        #点击所属部门下拉框
        self.find(*self._add_department_parent).click()
        #选中部门下拉框的元素
        self.find(*self._add_department_parentSelect).click()
        #点击提交按钮
        self.find(*self._add_department_sumbit).click()
        #返回通讯录对象
        from selenium_test.page_object.address_book import addressBook
        return addressBook(self._driver)
