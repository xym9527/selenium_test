from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

class basePage:
    def __init__(self,driver:WebDriver=None):
        if driver is None:
            self._driver=webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
            self._driver.get(self._base_url)
        else:
            self._driver=driver
    def close(self):
        sleep(10)
        self._driver.quit()

    def find(self, by, value):
        return self._driver.find_element(by=by,value=value)

    def finds(self, by, value):
        return self._driver.find_elements(by=by,value=value)

    def scrollToElement(self,el):
        self._driver.execute_script("arguments[0].scrollIntoView();", el)


