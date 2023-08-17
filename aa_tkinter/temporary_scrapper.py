from tkinter import *

root=Tk()
root.geometry("700x600")
root.title("Login Page")
root.config(bg="pink")

f1=Frame(root)
f1.pack(pady=30)

email=StringVar()
password=StringVar()

l1=Label(f1,text="Sign Up",font="helvetica 30 bold",fg="blue").pack(anchor="nw",padx=200,pady=50)
l2=Label(f1,text="Email-",font="helvetica 20 bold",fg="gray").pack(anchor="nw",padx=20,pady=50)

l3=Label(f1,text="Password-",font="helvetica 20 bold",fg="gray").pack(anchor="nw",pady=20)
l4=Label(f1,text="Already have an account",font="helvetica 15 bold",fg="yellow").pack(padx=10,anchor="nw",pady=20)

root.mainloop()
