import sqlite3
from tkinter import *
def saveinfo():
    
    pass
root=Tk()
root.geometry("700x600")
root.minsize(700,600)
root.maxsize(700,600)
root.title("Registration Form")
#Labels
Label(root,text="Registration Form",font=("arial",30,"bold")).pack(anchor="n")
Label(root,text="firstname",font=10).place(x=125,y=100)
Label(root,text="lastname",font=10).place(x=125,y=150)
Label(root,text="Email id",font=10).place(x=125,y=200)
Label(root,text="Phone no",font=10).place(x=125,y=250)
Label(root,text="Gender",font=10).place(x=125,y=300)
Label(root,text="Country",font=10).place(x=125,y=350)
Label(root,text="Progrmming",font=10).place(x=125,y=400)
Label(root,text="Preferrence",font=10).place(x=125,y=430)
#declaring variables
fname=StringVar()
fname.set("")
lname=StringVar()
lname.set("")
email=StringVar()
email.set("")
phone=IntVar()
phone.set("")
gender=StringVar()
gender.set(None)
countries=["India","Pakistan","Nepal","USA","England","China"]
country=StringVar()
country.set(countries[0])
programming=StringVar()
lang=["Python","Java","JavaScript","C","C++","R"]
programming.set(lang[0])
#entries
fname_entry=Entry(root,textvariable=fname).place(x=300,y=100)
lname_entry=Entry(root,textvariable=lname).place(x=300,y=150)
email_entry=Entry(root,textvariable=email).place(x=300,y=200)
phone_entry=Entry(root,textvariable=phone).place(x=300,y=250)
gender_entry=Radiobutton(root,text="male",variable=gender,value="male").place(x=300,y=300)
gender_entry=Radiobutton(root,text="female",variable=gender,value="female").place(x=370,y=300)
country_entry=OptionMenu(root,country,*countries).place(x=300,y=350)
p_entry=OptionMenu(root,programming,*lang).place(x=300,y=400)
B1=Button(root,text="Submit",command=saveinfo,font=("arial",20),bg="yellow").place(x=250,y=500)

root.mainloop()
