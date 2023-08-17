from tkinter import *

def getvals():
    print("Name=",namevalue.get())
    print("Course=",coursevalue.get())
    print("Address=",address_entry.get())
    print("father name=",father_name.get())
    
root=Tk()
root.title("Enter details")
root.geometry("600x600")
name=Label(root,text="name")
course=Label(root,text="course")
name.grid()
course.grid(row=1)
Label(root,text="address").grid(row=2)
Label(root,text="father name").grid(row=3)

namevalue=StringVar()
coursevalue=StringVar()
addvalue=StringVar()
fathervalue=StringVar()

name_entry=Entry(root,textvariable=namevalue)
course_entry=Entry(root,textvariable=coursevalue)
address_entry=Entry(root,textvariable=addvalue)
father_name=Entry(root,textvariable=fathervalue)

name_entry.grid(row=0,column=1)
course_entry.grid(row=1,column=1)
address_entry.grid(row=2,column=1)
father_name.grid(row=3,column=1)
Button(text="Submit",command=getvals).grid(row=5,column=5)
 
root.mainloop()
