# _*_ coding:utf-8 _*_
'''
Created on 2013-4-1

@author: huanghu
'''
import random
from com.queue.queue_entity import QueueEntity

class Porduct(object):
    def create(self):
        num = 0;
        queue = QueueEntity();
        while num < 1000:
            value = random.randrange(0 ,100);
            queue.setQueue(value);
            num = num +1;
        
            
        
        