# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:37:21 2021

@author: Rohit
"""
words=["donkey"]
with open("this","r") as f:
    text=f.read()
for word in words:
    if word in text:    
        text=text.replace("donkey","*****")
with open("this","w") as f:
    f.write(text)
    