from tkinter import *
from tkinter.messagebox import showinfo
import instaloader

root=Tk()
root.geometry("600x588")
root.title("Insta profile pic downloader")

def getdata():
    ig=instaloader.Instaloader()
    ig.download_profile(insta_id.get(),profile_pic_only=True)
    showinfo("Succesfully downloaded","Image saved in your internal memory")
    insta_id.set("")

l1=Label(root,text="Get anyone's profile from here",font="lucida 25 bold",fg="blue")
l1.pack()

l2=Label(root,text="Enter id",font="lucida 20")
l2.pack(pady=30,anchor="nw")

insta_id=StringVar()
insta_id.set("")

e1=Entry(root,textvariable=insta_id,font="lucida 15")
e1.pack(pady=10,anchor="nw")

b1=Button(root,text="Submit  ",font="helvetica 20 bold",fg="blue",command=getdata)
b1.pack()


root.mainloop()