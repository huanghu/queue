'''
Created on 2013-4-1

@author: huanghu
'''
import unittest
from com.customer.customer_main import Customer

class Test(unittest.TestCase):


    def setUp(self):
        self.customer = Customer();

    def testName(self):
        self.customer.take();


if __name__ == "__main__":
    unittest.main()