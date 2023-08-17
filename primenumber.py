# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 08:08:31 2021

@author: Rohit
"""
min=int(input("enter minimum limit:"))
max=int(input("enter maximum limit:"))
def prime_num(a,b):
    
    prime=[]
    for i in range(min,max):
        for j in range(2,i-1):
            if i%j==0:
                break
        else:
            prime.append(i)
    return prime
print(f"prime numbers between {min} and {max} are:{prime_num(min,max)}")
def armstrong(a,b):
    armst=[]
    for i in range(a,b):
        i=str(i)
        l=len(i)
        sum=0
        for j in i:
            sum+=int(j)**l
        if sum==int(i):
            armst.append(i)
    return armst
print(f"armstrong numbers between {min} and {max} are:{armstrong(min,max)}")
           
        
        