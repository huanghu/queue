# _*_ coding:utf-8 _*_
'''
Created on 2013-4-1

@author: huanghu
'''
from Queue import Queue

class QueueEntity:
    def __init__(self):
        pass
    
    #往队列放入元素
    def setQueue(self ,value):
        global queue;
        if queue.qsize() < 1000:
            queue.put(value);
    
    #从队列取出元素    
    def getQueue(self):
        global queue;
        if queue.qsize() >= 0:
            value = queue.get();
            return value;
            

queue = Queue();