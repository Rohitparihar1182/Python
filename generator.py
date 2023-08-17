# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:09:01 2021

@author: Rohit
"""
'''
a=int(input("enter a number"))
b=int(input("enter a number"))
ans=(a+b)**2
print(ans)


'''
def rev(a):
    reversed_str=a[::-1]
    yield reversed_str

str="Rohit"
str=rev(str)
print(next(str))
#or
for i in str:
    print(i)

