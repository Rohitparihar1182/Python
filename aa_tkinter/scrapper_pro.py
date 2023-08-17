from tkinter import *
import tkinter.messagebox as tmsg
from bs4 import BeautifulSoup
import smtplib
import time
import requests

def end():
    global a
    if a==1:
        tmsg.showinfo("Done!!","Hey your request has been submitted")
    if price<=int(expexted_cost.get()):
        sendmail()
    a+=1
def sendmail():
    global mail
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("deadprogrammer1810@gmail.com","zpubkjbffxqmkfvm")
    subject="Price fell down!"
    body="Check the link-https://www.amazon.in/Sennheiser-Wired-Hi-End-Headphone-Amplifier/dp/B002NV1J2C/ref=sr_1_2?dchild=1&keywords=headphones&qid=1618226138&sr=8-2"
    msg=f"{subject}\n\n{body}"
    server.sendmail("deadprogrammer1810@gmail.com","mail",msg)
    print("EMAIL HAS BEEN SENT...")    

    server.quit()

def real_price(price):
    temp=""
    for i in price:
        if i!=0 :
            if i!=",":
                if i==".":
                    break
                temp+=i
    price=int(temp)
    return price

def check_price():
    global price,mail
    
    header={"user agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
    url=URL.get()
    page=requests.get(url,headers=header)

    soup=BeautifulSoup(page.content,"html.parser")

    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    tmsg.showinfo("Price!!",f"The price of the product is {price}")
    info=tmsg.askquestion("Wanna get a mail??","Wanna get notofied when the price fall down??")
    price=real_price(price[1:])
    if info=="yes":
        f1.pack_forget()
        f2=Frame(root)
        f2.pack()
        l3=Label(f2,text="Enter your mail id below!!",font=("lucida",30,"bold"))
        l3.pack()
        
        e2=Entry(f2,textvariable=mail,width=100,font=("lucida",30))
        e2.pack(padx=20,pady=30)

        l4=Label(f2,text="Enter your expexted price!!",font=("lucida",30,"bold"))
        l4.pack()
        
        e3=Entry(f2,textvariable=expexted_cost,width=100,font=("lucida",30))
        e3.pack(padx=20,pady=30)

        b2=Button(f2,text="Submit ",font=("lucida",30,"bold"),command=end)
        b2.pack(padx=20,pady=30)
        
        
root=Tk()
root.geometry("700x700")

root.configure(bg="gray")

f1=Frame(root,bg="gray")
f1.pack()

URL=StringVar()
URL.set("")
expexted_cost=StringVar()
expexted_cost.set("")
mail=StringVar()
mail.set("")
price=""
a=1
def main():

    l1=Label(f1,text="Welcome to an amazing web Scrapper",font=("lucida",30,"bold"),fg="white",bg="yellow")
    l1.pack()

    l2=Label(f1,text="Enter the link of the product:",font=("lucida",25,"bold"),fg="white",bg="black")
    l2.pack(side=LEFT,anchor="nw",pady=30)

    e1=Entry(f1,textvariable=URL)
    e1.place(x=20,y=150,width=300,height=50)

    b1=Button(f1,text="Check price",font=("arial",20,"bold"),command=check_price)
    b1.pack(side=LEFT,pady=300)

main()

root.mainloop()
