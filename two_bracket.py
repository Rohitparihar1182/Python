# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 08:10:00 2021

@author: Rohit
"""


str1=input("enter string")
str1=list((str1))
for i in str1:
    if i=="["or']'or'('or')':
        del str1[i]
print(str1)
'''a=0
b=0
c=0
d=0
for i in str1:
    if i=="[":
        a+=1
    elif i=="]":
        b+=1
    elif i=="(":
        c+=1
    elif i==")":
        d+=1
if a>=b:
    k=b
elif b>a:
    k=a
if c>=d:
    k+=d
elif d>c:
    k+=c
print(k)
        
#for checking one time only
if "[" and "]" in str1:
    k=1
    if "(" and ")" in str1:
        k=2
elif "(" and ")" in str1:
    k=1
print(k)
'''