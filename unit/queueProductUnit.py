# _*_ coding:utf-8 _*_
'''
Created on 2013-4-1

@author: huanghu
'''
import unittest
from com.product.product_main import Porduct
from com.customer.customer_main import Customer

class Test(unittest.TestCase):

    def setUp(self):
        self.product = Porduct();
        self.customer = Customer();

    def testName(self):
        self.product.create();
        msg = self.customer.take();
        print "take " + str(msg);

if __name__ == "__main__":
    unittest.main()