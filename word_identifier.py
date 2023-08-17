# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 18:18:46 2021

@author: Rohit
"""

str=input("enter :-")
if str.isalnum():
    print("entered value is alphanumeric...")
elif str.isnumeric():
    print("entered value is numeric...")
elif str.isupper():
    print("entered value is uppercase...")
elif str.islower():
    print("entered value is lowercase...")
elif str.isspace():
    print("you entered blank space")
else:
    print("entered value is special character...")
    