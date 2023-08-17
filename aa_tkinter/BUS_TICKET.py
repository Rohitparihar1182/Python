from tkinter import *
def getvals():
    print("your record has been taken ")
    print("Have a nice journey")
    with open("record.txt","a") as f:
        f.write(f"{name.get()},{phone.get()},{gender.get()},{paymentmode.get()},{foodservice.get()}\n")
root=Tk()
root.geometry("600x400")
Label(root,text="Welcome to Rohit travels",bg="red",fg="black",font=("baskerville",20,"bold"),relief=SUNKEN).grid(row=0,column=3)
Label(root,text="name").grid(row=1,column=2)
Label(root,text="phone").grid(row=2,column=2)
Label(root,text="gender").grid(row=3,column=2)
Label(root,text="paymentmode").grid(row=4,column=2)

#taking details
name=StringVar()
phone=IntVar()
gender=StringVar()
paymentmode=StringVar()
foodservice=IntVar()


#assigning values
name_entry=Entry(root,textvariable=name)
phone_entry=Entry(root,textvariable=phone)
gender_entry=Entry(root,textvariable=gender)
pay_entry=Entry(root,textvariable=paymentmode)


#packing entries
name_entry.grid(row=1,column=3)
phone_entry.grid(row=2,column=3)
gender_entry.grid(row=3,column=3)
pay_entry.grid(row=4,column=3)

#checkbutton&pack
food_service=Checkbutton(text="want to prebook your meal",variable=foodservice)
food_service.grid(row=5,column=3)


#button
Button(text="submit to Rohit travels",command=getvals).grid(row=6,column=4)


root.mainloop()
