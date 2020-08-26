from time import time

from selenium_test.page_object.index_page import indexPage

class TestIndex:
    def setup_class(self):
        self.index=indexPage()
        self.index.add_cookies()

    def teardown_class(self):
        self.index.close()

    #添加成员
    def test_addMenber(self):
        name="回合"
        phone="13100010002"
        result=self.index.goto_add_member().add_member(name,phone).get_member_list()
        assert name in ' '.join(result)

    #删除成员
    def test_delMember(self):
        name='回合'
        self.index.goto_addressBook().del_member(name)

    #导入通讯录
    def test_importAddressBook(self):
        self.index.goto_index().goto_import_addressBook().import_addressBook()
        #回到首页
        self.index.goto_index()

    #添加部门
    def test_addDepartment(self):
        name="回合"
        result=self.index.goto_addressBook().goto_add_department().add_department(name).get_department_list()
        assert name in ' '.join(result)
