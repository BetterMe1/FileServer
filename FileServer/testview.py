# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver

class Testview(unittest.TestCase):
    #初始化环境
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)   #等待30s
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_view(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_xpath(u"(//a[contains(text(),'查看')])[2]").click()
        driver.implicitly_wait(30)
        handles = driver.window_handles
        print(handles)
        driver.switch_to.window(handles[1])
        print (driver.current_window_handle)
        print (driver.title)
        print (driver.current_url)
        driver.quit()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
    if __name__ == "__main__":
        unittest.main()

