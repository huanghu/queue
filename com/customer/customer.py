'''
Created on 2013-4-1

@author: huanghu
'''
from com.queue.queue_entity import QueueEntity

class Customer(object):
    '''
    classdocs
    '''
    def take(self):
        queue = QueueEntity()
        msg = queue.getQueue();
        return msg;