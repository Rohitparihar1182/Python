# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:46:49 2021

@author: Rohit
"""
import random
a="abcdefghijklmnopqrstuvxyz"
b=a.upper()
c="0123456789"
d="@#%&?!"
p=a+b+c+d
password=""
for i in range(8):
    l=len(p)
    x=random.randint(0,l)
    password+=p[x]
print(password)