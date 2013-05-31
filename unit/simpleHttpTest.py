'''
Created on 2013-4-2

@author: huanghu
'''
import unittest
import SimpleHTTPServer

class Test(unittest.TestCase):


    def setUp(self):
        pass;
    
    def testName(self):
        SimpleHTTPServer.test()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()