# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:24:55 2021

@author: Rohit
"""

class Company:
    def enter_detail(self):
        self.name=input("enter name")
        self.gender=input("enter your gender")
        self.salary=int(input("enter your salary"))
    def get_detail(self):
        if self.gender=="m":
            if self.salary<10000:
                self.bonus=self.salary*(7/100)
                self.salary+=self.bonus
            else:
                self.bonus=self.salary*(5/100)
                self.salary+=self.bonus
        else:
            if self.salary<10000:
                self.bonus=self.salary*(12/100)
                self.salary+=self.bonus
            else:
                self.bonus=self.salary*(10/100)
                self.salary+=self.bonus
        print(f"hey {self.name} your bonus is {self.bonus}\
and salary is {self.salary}")

x=Company()
x.enter_detail()
x.get_detail()

