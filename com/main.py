'''
Created on 2013-4-1

@author: huanghu
'''
from com.product.product import Porduct
from com.queue.queue_server import QueueServer

if __name__ == '__main__':
    product = Porduct();
    product.create();
    service = QueueServer();
    service.examBaseHTTP();