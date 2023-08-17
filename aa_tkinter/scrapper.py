import requests
from bs4 import BeautifulSoup
import smtplib
import time

    
def cost_converter(x):
    temp=""
    for i in x:
        if i==",":
            pass
        else:
            temp+=i
    return int(temp)

URL="https://www.amazon.in/Sennheiser-Wired-Hi-End-Headphone-Amplifier/dp/B002NV1J2C/ref=sr_1_2?dchild=1&keywords=headphones&qid=1618226138&sr=8-2"

header={"user agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}

def check_price():

    page=requests.get(URL,headers=header)

    soup=BeautifulSoup(page.content,"html.parser")

    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    real_price=price[1:10]

    real_price=cost_converter(real_price)

    print(title.strip())
    print(real_price)
    if real_price<140000:
        sendmail()


def sendmail():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("rohitsinghparihar78384@gmail.com","hijjgnmraeevffqc")
    subject="Price fell down!"
    body="Check the link-https://www.amazon.in/Sennheiser-Wired-Hi-End-Headphone-Amplifier/dp/B002NV1J2C/ref=sr_1_2?dchild=1&keywords=headphones&qid=1618226138&sr=8-2"
    msg=f"{subject}\n\n{body}"
    server.sendmail(
        "rohitsinghparihar78384@gmail.com",
        "rohitsinghparihar967@gmail.com",msg
    )
    print("EMAIL HAS BEEN SENT...")    

    server.quit()
check_price()

#for checking the price daily
'''
while(True):
    check_price()
    time.sleep(24*60*60)
'''