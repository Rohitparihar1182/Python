# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:11:37 2021

@author: Rohit
"""

def hcf(num1,num2):
    if num1>num2:
        num1,num2=num2,num1

    for i in range(1,num1+1):
        if (num1%i==0) & (num2%i==0):
            hcf=i
    return hcf
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print(f"HCF of {a} and {b} is = {hcf(a,b)}")
