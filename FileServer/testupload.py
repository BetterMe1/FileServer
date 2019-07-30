# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver

class Testupload(unittest.TestCase):
    #初始化环境
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)   #等待30s
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_upload(self):
        driver = self.driver;
        driver.get(self.base_url+"/")
        driver.find_element_by_name("filename").clear()
        driver.find_element_by_name("filename").send_keys(u"C:\\Users\\lenovo\\Desktop\\元素\\1.doc")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click();
        driver.implicitly_wait(30)
        if(driver.find_element_by_link_text(u"1.png")).is_displayed():
            print"上传成功"
        else:
            print"上传失败"
        driver.quit()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
    if __name__ == "__main__":
        unittest.main()