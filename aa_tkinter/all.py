from tkinter import *
#starting
obj=Tk()

obj.geometry("600x400")
#obj.minsize(400,200)
#obj.maxsize(800,800)
obj.title("Rohit's GUI")
#adding labels
#inside pack we can add side,anchor,fill etc....

l1=Label(obj,text="Hey there I am your boss Rohit Singh Parihar",fg="red",bg="black",padx=20,pady=20,font=("arial",15,"bold"),borderwidth=3,relief=SUNKEN)

l1.pack(anchor="nw")

#creating a function for our button

def my():
    print("Ok")

#adding frame
f1=Frame(obj,bg="blue",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
l2=Label(f1,text="hii")
l2.pack(pady=100,padx=40)
f2=Frame(obj,bg="blue",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
l3=Label(f2,text="hii again",font=("arial",10))
l3.pack(padx=100,pady=50) 

#adding buttons

b1=Button(obj,text="submit",font=("jokerman",15),command=my,relief=RIDGE)
b1.pack()






obj.mainloop()

