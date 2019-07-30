# -*- coding: utf-8 -*-
import os
import unittest
from selenium import webdriver

class Testdown(unittest.TestCase):
    #初始化环境
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)   #等待30s
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_down(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_link_text(u"1.png").click()
        driver.implicitly_wait(30)
        if os.path.exists(u"C:\\Users\\lenovo\\Desktop\\元素\\1.doc"):
            print "下载成功"
        else:
            print "下载失败"
        driver.quit()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
    if __name__ == "__main__":
        unittest.main()