from tkinter import *
import phonenumbers
from phonenumbers import timezone,geocoder,carrier

def getdata():
    phone=phonenumbers.parse("phone_num")

    timezone=timezone.time_zones_for_number(phone)

    Carrier=carrier.name_for_number(phone,'en')

    region=geocoder.description_for_number(phone,'en')

    l3=Label(root,text=f"")

root=Tk()
root.geometry("600x500")
#root.configure(bg="gray")

l1=Label(root,text="Get any number's detail here",font="lucida 25 bold",fg="blue")
l1.pack()

l2=Label(root,text="Enter the number...",font="lucida 20")
l2.pack(pady=30,anchor="nw")

phone_num=StringVar()
phone_num.set("+91")

e1=Entry(root,textvariable=phone_num,font="lucida 15")
e1.pack(pady=10,anchor="nw")

b1=Button(root,text="Get data",font="helvetica 20 bold",fg="blue",command=getdata)
b1.pack()
root.mainloop()