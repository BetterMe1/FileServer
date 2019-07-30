# -*- coding: utf-8 -*-
import unittest
from FileServer import testupload, testview,testdown,testdelete

#批量执行
def createsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testupload.Testupload))
    suite.addTest(unittest.makeSuite(testview.Testview))
    suite.addTest(unittest.makeSuite(testdown.Testdown))
    suite.addTest(unittest.makeSuite(testdelete.Testdelete))
    return suite

if __name__=="__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
