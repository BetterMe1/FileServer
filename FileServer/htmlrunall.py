# -*- coding: utf-8 -*-
#手工添加案例到套件
import HTMLTestRunner
import os
import sys
import time
import unittest

from FileServer import testupload, testview, testdown, testdelete


def createsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testupload.Testupload))
    suite.addTest(unittest.makeSuite(testview.Testview))
    suite.addTest(unittest.makeSuite(testdown.Testdown))
    suite.addTest(unittest.makeSuite(testdelete.Testdelete))
    return suite

if __name__=="__main__":
    curpath=sys.path[0]
    #取当前时间
    now=time.strftime("%Y-%m-%d-%H %M %S",time.localtime(time.time()))
    if not os.path.exists(curpath+'/resultreport'):
        os.makedirs(curpath+'/resultreport')
    filename=curpath+'/resultreport/'+now+'resultreport.html'
    with open(filename,'wb') as fp:
        #出html报告
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况',verbosity=2)
        suite=createsuite()
        runner.run(suite)