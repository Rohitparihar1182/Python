from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("799x866")
root.title("Weight Conversiom")
options=["kg","g","pound","ounce"]

def calculate():
    global options
    if var1.get()=="Select unit":
        tmsg.showinfo("Select a unit","Input unit not defined")
        return 0
    elif var1.get()==options[0]:
        if var2.get()==options[0]:
            value=x.get()
            value=str(value)
            ans=value+"kg"
        elif var2.get()==options[1]:
            value=(x.get()*1000)
            value=str(value)
            ans=value+"g"
        elif var2.get()==options[2]:
            value=(x.get()*2.205)
            value=str(value)
            ans=value+"pounds"
        elif var2.get()==options[3]:
            value=(x.get()*35.275)
            value=str(value)
            ans=value+"ounce"
    elif var1.get()==options[1]:
        if var2.get()==options[0]:
            value=x.get()/1000
            value=str(value)
            ans=value+"kg"
        elif var2.get()==options[1]:
            value=x.get()
            value=str(value)
            ans=value+"g"
        elif var2.get()==options[2]:
            value=(x.get()*2.205)/1000
            value=str(value)
            ans=value+"pounds"
        elif var2.get()==options[3]:
            value=(x.get()*35.275)/1000
            value=str(value)
            ans=value+"ounce"
    elif var1.get()==options[2]:
        if var2.get()==options[0]:
            value=x.get()*0.453
            value=str(value)
            ans=value+"kg"
        elif var2.get()==options[1]:
            value=x.get()*453.59
            value=str(value)
            ans=value+"g"
        elif var2.get()==options[2]:
            value=x.get()
            value=str(value)
            ans=value+"pounds"
        elif var2.get()==options[3]:
            value=x.get()*16
            value=str(value)
            ans=value+"ounce"
    elif var1.get()==options[3]:
        if var2.get()==options[0]:
            value=x.get()*0.028
            value=str(value)
            ans=value+"kg"
        elif var2.get()==options[1]:
            value=x.get()*28.349
            value=str(value)
            ans=value+"g"
        elif var2.get()==options[2]:
            value=x.get()*0.0625
            value=str(value)
            ans=value+"pounds"
        elif var2.get()==options[3]:
            value=x.get()
            value=str(value)
            ans=value+"ounce"         
    if var2.get()=="Select unit":
        tmsg.showinfo("Select a unit","Output unit not defined")
        return 0
    l3=Label(root,text=ans,font=("arial",30))
    l3.place(x=200,y=300)

#variabels
var1=StringVar()
var1.set("Select unit")
var2=StringVar()
var2.set("Select unit")

x=IntVar()
ans=0

#entry widgets
l1=Label(root,text="Enter weight",font=("lucida",20,"bold"))
l1.place(x=50,y=50)
e1=Entry(root,textvariable=x,font=("lucida",18))
e1.place(x=50,y=100,height=30,width=140)


op1=OptionMenu(root,var1,*options)
op1.place(x=200,y=100)

l1=Label(root,text="Select output unit",font=("lucida",20,"bold"))
l1.place(x=500,y=50)
op2=OptionMenu(root,var2,*options)
op2.place(x=600,y=100)

b1=Button(root,text="Convert",fg="blue",borderwidth=2,font=("arial",20,"bold"),command=calculate)
b1.place(x=600,y=200)


root.mainloop()