# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver

class Testdelete(unittest.TestCase):
    #初始化环境
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)   #等待30s
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_delete(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[2]").click()
        driver.implicitly_wait(30)
        print "删除成功"
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
    if __name__ == "__main__":
        unittest.main()