from tkinter import *
import tkinter.messagebox as tmsg
from bs4 import BeautifulSoup
import smtplib
import time
import requests

def sendmail():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("deadprogrammer1810@gmail.com","zpubkjbffxqmkfvm")
    subject="Price fell down!"
    body="Check the link-https://www.amazon.in/Sennheiser-Wired-Hi-End-Headphone-Amplifier/dp/B002NV1J2C/ref=sr_1_2?dchild=1&keywords=headphones&qid=1618226138&sr=8-2"
    msg=f"{subject}\n\n{body}"
    server.sendmail(
        "deadprogrammer1810@gmail.com",
        "rohitsinghparihar967@gmail.com",msg
    )
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


def Check_Price():
    global price,mail
    if URL.get()=="":
        tmsg.showinfo("Enter a link","Link cannot be empty")
        
    else:
        header={"user agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
        url=URL.get()
        page=requests.get(url,headers=header)

        soup=BeautifulSoup(page.content,"html.parser")

        title=soup.find(id="productTitle").get_text()
        price=soup.find(id="priceblock_ourprice").get_text()
        l3=Label(root,text="Price-",font=("arial",20,"bold"),fg="red")
        l3.place(x=40,y=250)
        l4=Label(root,text=f"{price}",font=("arial",20,"bold"),fg="red")
        l4.place(x=140,y=250)
        price=real_price(price[1:])
        print(price)
        time.sleep(3)
        mail_info=tmsg.askquestion("Wanna get a mail???","Wanna get notified when the price falls down")
        if mail_info=="yes":
            


        elif mail_info=="no":
            print("okay")
 

def display():

    l1=Label(f1,text="Scrapper",font=("arial",30,"bold"),fg="red")
    l1.place(x=200,y=50)
    
    l2=Label(f1,text="Enter the link here...",font=("arial",20,"bold"),fg="blue")
    l2.place(x=40,y=140)
    e1=Entry(f1,textvariable=URL,font=("lucida",15),width=22,relief=GROOVE, borderwidth=5)
    e1.place(x=40,y=180)
    b1=Button(f1,text="Check price",font=("lucida",15,"bold"),relief=GROOVE, borderwidth=2,command=Check_Price)
    b1.place(x=300,y=180)


root=Tk()
root.geometry("600x400")
root.configure(bg="gray")
root.title("Scrapper")
root.resizable(False,False)
f1=Frame(root).pack()
price=""
mail_info=""
URL=StringVar()
URL.set("")
display()

   

root.mainloop()
