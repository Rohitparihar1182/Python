from tkinter import *
def add():
    print(f"{int(a.get())}+{int(b.get())}={int(a.get())+int(b.get())}")
def sub():
    print(f"{int(a.get())}-{int(b.get())}={int(a.get())-int(b.get())}")
def mul():
    print(f"{int(a.get())}*{int(b.get())}={int(a.get())*int(b.get())}")
def div():
    print(f"{int(a.get())}/{int(b.get())}={int(a.get())/int(b.get())}")
rohit=Tk()
rohit.geometry("600x600")
rohit.title("Welcome to my calculator")

a=StringVar()
b=StringVar()

num1_entry=Entry(rohit,textvariable=a)
num1_entry.grid()

num2_entry=Entry(rohit,textvariable=b)
num2_entry.grid()


Button(rohit,text="      +      ",borderwidth=6,padx=30,command=add).grid(row=3,column=3)
Button(rohit,text="      -      ",borderwidth=6,padx=30,command=sub).grid(row=4,column=3)
Button(rohit,text="      *      ",borderwidth=6,padx=30,command=mul).grid(row=5,column=3)
Button(rohit,text="      /      ",borderwidth=6,padx=30,command=div).grid(row=6,column=3)





rohit.mainloop()
