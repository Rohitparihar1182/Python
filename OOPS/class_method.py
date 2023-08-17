# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 22:27:13 2021

@author: Rohit
"""

#class method
class test():
    
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def print_data(self):
        print("name=",self.name)
        print("age=",self.age)
        print("course=",self.course)
    @classmethod
    def class_method(cls,name,age,course):
        print("name=",name)
        print("age=",age)
        print("course=",course)        
    @staticmethod
    def static_method(name,age):
        print("name=",name)
        print("age=",age)
t1=test("Rohit",20,"BCA")
t1.print_data()
#for class method
t1.class_method("Sarge",21,"BCA")
#for statix method
t2=test.static_method("Rohit",22)
