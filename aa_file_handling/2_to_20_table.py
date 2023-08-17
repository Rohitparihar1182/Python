# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:18:14 2021

@author: Rohit
"""

for i in range(2,21):
    with open(f"table_of_{i}.txt","a") as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}\n")
            
        