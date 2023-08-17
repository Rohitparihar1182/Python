from tkinter import *
import tkinter.messagebox as tmsg
from PyDictionary import PyDictionary

my_dict=PyDictionary()

def Check():
    options=[my_dict.meaning(word.get()),my_dict.synonym(word.get()),my_dict.antonym(word.get())]
    print(options[0])
    for i in range(3):
        label=Label(root,text=options[i],bg="blue",font="helvetica 20")
        label.place(x=500,y=(260+i*70))

root=Tk()
root.geometry("799x877")
root.title("Advanced Dictionary")
root.resizable(False,False)
root.config(bg="black")
word=StringVar()
word.set("")

l1=Label(root,text="Enter your word here...",font="helvetica 30 bold",bg="blue").pack()
e1=Entry(root,textvariable=word,width=30,relief=SUNKEN,font="arial 20").pack(pady=80)
b1=Button(root,text="Check",fg="blue",bg="black",font="arial 18 bold",command=Check,relief=SUNKEN)
b1.place(x=560,y=180)

options=["Meaning ","Synonym","Antonym "]
for i in range(3):
    label=Label(root,text=options[i],bg="blue",font="helvetica 20")
    label.place(x=200,y=(260+i*70))


root.mainloop()
