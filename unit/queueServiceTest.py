'''
Created on 2013-3-29

@author: huanghu
'''
import unittest
from com.queue.queue_server import QueueServer

class QueueServiceTest(unittest.TestCase):
    
    def setUp(self):
        self.service = QueueServer();
    
    def testName(self):
        print 'begin';
        self.service.examBaseHTTP();
        

if __name__ == "__main__":
    unittest.main()