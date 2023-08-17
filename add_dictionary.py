# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:22:52 2021

@author: Rohit
"""

dict1={"a":1,"b":45,"c":76}
dict2={"c":3,"b":76,"z":34}
new_dict=dict1.copy()
for key in dict2:
    if key in new_dict:
        new_dict[key]=dict1[key]+dict2[key]
    else:
        new_dict[key]=dict2[key]
    
print(new_dict)
