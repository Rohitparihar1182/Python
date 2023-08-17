from tkinter import *
import tkinter.messagebox as tmsg
from bs4 import BeautifulSoup
import smtplib
import time
import requests


def SendMail():
    GMailid="rohitsinghparihar967@gmail.com"
    
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('deadprogrammer1810@gmail.com','xvasvnrayedzejua')
    subject="Price fell down!"
    body="Check the link-"
    msg=f"Subject: {subject}\n\n{body}"
    server.sendmail('deadprogrammer1810@gmail.com',GMailid,msg)
    print("EMAIL HAS BEEN SENT...")    

    server.quit()

SendMail()
