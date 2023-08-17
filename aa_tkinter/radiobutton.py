from tkinter import *
import tkinter.messagebox as tmsg
def order():
    if var.get()=="none":
        tmsg.showinfo("Order not Placed","You have not still placed any order")
    else:
        tmsg.showinfo("Order Placed",f"{var.get()} khayega ? bhag......") 
root=Tk()
root.geometry("600x600")
root.title("Kammu's restaurant")
#declaring variable
var=StringVar()
var.set("none")
#list of food
food=["Burger","Chowmene","Momos","Chole Bhature"]
#labeling text
Label(root,text="Welcome sir what would you like to have?",font=("lucida",19,"bold"),justify=CENTER).pack()
#adding food options
for i in range(4):
    radio=Radiobutton(root,text=food[i],pady=20,variable=var,value=food[i]).pack(anchor="w")
Button(root,text="Place order",command=order).pack()










root.mainloop()
