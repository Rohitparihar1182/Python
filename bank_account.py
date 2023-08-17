# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 14:36:20 2021

@author: Rohit
"""
import random
class Bank:
    def enter_detail(self):
        self.name=input("enter your name:")
        self.address=input("enter your address:")
        self.dob=input("enter your date of birth:")
        self.gender=input("enter your gender:")
    def acc_num(self):
        self.acc_num=random.randint(1111111111111111,999999999999999999)
        self.amount=0
        if self.gender=="m"or"male":
            print(f"Hey mr. {self.name} your account number is {self.acc_num}")
        elif self.gender=="f"or"female":
            print(f"Hey mrs. {self.name} your account number is {self.acc_num}")
    def deposit(self):
        amount=int(input("enter amount:"))
        if self.amount<1000:
            print("Can't deposit less than 1000:")
        else:
            self.amount+=amount
    def withdraw(self):
        amount=input("enter amount:")
        if amount<self.amount:
            print("not enough balance...")
        elif amount<1000:
            print("can't withdraw less than 1000.....")
        else:
            self.amount-=amount
    def check_bal(self):
        print("Your account total amount:",self.amount)
b=Bank()
b.enter_detail()
b.acc_num()
temp="yes"
while temp=="yes":
    temp=input('''press 1 to deposit)
press 2 to withdraw
press 3 to check balance
press 4 to exit
enter:''')
    if temp==1:
        b.deposit()
    elif temp==2:
        b.withdraw()
    elif temp==3:
        b.check_bal()
    else:
        break
    temp="yes"

            
