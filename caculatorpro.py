# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 08:17:38 2021

@author: Rohit
"""

class Calculator:
    def square(self):
        num=int(input("enter the number:"))
        print("square of given number is=",num**2)
    def cube(self):
        num=int(input("enter the number:"))
        print("cube of given number is=",num**3)
    def sqrt(self):
        num=int(input("enter the number:"))
        print("square root of given number is=",num**(0.5))
c=Calculator()
x=int(input('''1 for square
2 for cube
3 for square root
enter:-'''))
if x==1:
    c.square()
elif x==2:
    c.cube()
elif x==3:
    c.sqrt()
else:
    print("invalid input")
    