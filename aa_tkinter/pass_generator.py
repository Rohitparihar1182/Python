# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:46:49 2021

@author: Rohit
"""
import random
from tkinter import *
import tkinter.messagebox as tmsg
def password():
    a="abcdefghijklmnopqrstuvxyz"
    b=a.upper()
    c="0123456789"*2
    d="@#%&?!"
    p=a+b+c+d
    password=""
    for i in range(pass_word.get()):
        l=len(p)
        x=random.randint(0,l)
        password+=p[x-1]
    
    tmsg.showinfo("Here is your password",f"Password={password}")
    

root=Tk()
root.geometry("700x600")
root.title("Password Generator")
l1=Label(root,text="Select password length",bg="yellow",fg="red",font=("arial",30,"bold"))
l1.pack()
pass_word=Scale(root,from_=0,to=10,length=500,width=20,orient=HORIZONTAL,tickinterval=1)
pass_word.pack()
Button(root,text="Get Password",font=("arial",15),command=password).pack()

root.mainloop()
