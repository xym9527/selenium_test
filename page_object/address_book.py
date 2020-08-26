from selenium_test.page_object.base_page import *


class addressBook(basePage):

    #导航首页元素
    _index_=(By.CSS_SELECTOR,'[id="menu_index"]')

    #通讯录添加成员页面元素
    _add_member_= (By.CSS_SELECTOR,'[class="qui_btn ww_btn js_add_member"]')

    #通讯录导入通讯录页面元素
    _import_addressBook_=(By.CSS_SELECTOR,'.ww_btn_PartDropdown_left:nth-child(2)')
    _import_addressBookList_=(By.CSS_SELECTOR,\
                              '[class="qui_dropdownMenu_itemLink ww_dropdownMenu_itemLink js_import_member"]')

    #通讯录添加部门页面元素
    _add_department_=(By.CSS_SELECTOR,'[class="member_colLeft_top_addBtnWrap js_create_dropdown"]')
    _add_departmentList_=(By.CSS_SELECTOR,'.js_create_party')



    #通讯录成员列表
    _memberNameList=(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
    # 通讯录部门列表
    _departmentList=(By.CSS_SELECTOR,\
                     '[class="jstree-node js_editable jstree-last jstree-open"] a')

    #删除成员
    _memberCheck=(By.XPATH,'//*[@id="member_list"]//td[@title="回合"]/../td[1]')
    _del_member_button = (By.CSS_SELECTOR, \
                          '[class="js_operationBar_footer ww_operationBar"] [class="qui_btn ww_btn js_delete"]')
    _del_ack_button=(By.CSS_SELECTOR,'[class="qui_btn ww_btn ww_btn_Blue"]')

    #点击跳转到添加成员页
    def goto_add_member(self):
        self.find(*self._add_member_).click()

        from selenium_test.page_object.add_member import addMember
        return addMember(self._driver)

    # 点击弹窗添加部门
    def goto_add_department(self):
        self.find(*self._add_department_).click()
        self.find(*self._add_departmentList_).click()

        from selenium_test.page_object.add_department import addDepartment
        return addDepartment(self._driver)



    # 点击导入通讯录
    def goto_import_addressBook(self):
        self.find(*self._import_addressBook_).click()
        self.find(*self._import_addressBookList_).click()

        from selenium_test.page_object.import_addressBook import improtAddressBook
        return improtAddressBook(self._driver)

    # 获取通讯录页的成员列表
    def get_member_list(self):
        memberList=self.finds(*self._memberNameList)
        nameList=[]
        [nameList.append(name.text) for name in memberList]
        return nameList

    # 获取通讯录页的部门列表
    def get_department_list(self):
        self._driver.refresh()
        departmentList=self.finds(*self._departmentList)
        nameList = []
        [nameList.append(name.text) for name in departmentList]

        return nameList

    # 删除指定得成员
    def del_member(self,name):
        name=name
        self.find(*self._memberCheck).click()
        self.find(*self._del_member_button).click()
        self.find(*self._del_ack_button).click()

    # 点击导航回到首页
    def goto_index(self):
        self.find(*self._index_).click()

        from selenium_test.page_object.index_page import indexPage
        return indexPage(self._driver)

