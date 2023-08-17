from tkinter import *
import tkinter.messagebox as tmsg

a=1
def rating():
    global a
    with open("rating.txt","a") as f:
        f.write(f"user {a} rated {rate.get()}*\n")
    a+=1
    tmsg.showinfo("Thanks","Thanks for your great review")
root=Tk()
root.geometry("600x600")
Label(root,text="Kindly Rate Us ",font=("arial",15)).grid(row=1,column=0)
rate=Scale(root,from_=0,to=10,length=500,width=20,orient=HORIZONTAL,tickinterval=1)
rate.grid()
Button(root,text="Submit",font=("arial",15),command=rating,).grid()



root.mainloop()        
