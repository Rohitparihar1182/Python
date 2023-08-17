# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 20:51:35 2021

@author: Rohit
"""

def data():
    name=input("enter name:")
    phone=int(input("phone:"))
    salary=int(input("enter salary:"))
    return(name,phone,salary)
def output(a):
    print("name=",a[0])
    print("phone no.",a[1])
    print("salary",a[2])
a=data()
output(a)    
