from tkinter import *

def correct():
    print("correct answer")
def wrong():
    print("wrong answer")
root=Tk()
root.title("hey there")
root.geometry("800x400")

f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
l=Label(f1,text="who is our pm").pack()
b1=Button(f1,fg="red",text="Narendra Modi",command=correct)
b1.pack(side=LEFT)

b2=Button(f1,fg="red",text="Rahul Gandhi",command=wrong)
b2.pack(side=LEFT)

b3=Button(f1,fg="red",text="Arvind Kejriwal",command=wrong)
b3.pack(side=LEFT)

b4=Button(f1,fg="red",text="Yogi Adityanath",command=wrong)
b4.pack(side=LEFT)

root.mainloop()
