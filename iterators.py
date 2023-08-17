# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:42:52 2021

@author: Rohit
"""

class test:
    def __init__(self,max):
        self.max=max
    def __iter__(self):
        self.start=0
        return self
    def __next__(self):
        if self.start<=self.max:
            print(self.start)
            self.start+=1
        else:
            raise StopIteration
obj=test(5)
num=iter(obj)
for i in range(8):
   next(num)
