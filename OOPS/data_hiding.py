# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 21:57:42 2021

@author: Rohit
"""

class myclass:
    __num=20
    def add(self,a):
        sum=self.__num+a
        print(sum)
ob=myclass()
ob.add(5)
print(ob.__num)
