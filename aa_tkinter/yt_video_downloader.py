from tkinter import *
from pytube import YouTube
def yt():
    link=url_entry.get()
    ytvideo=YouTube(link)
    print(ytvideo.streams.filter(res='720p',progressive="True").first().download())

root=Tk()
root.geometry("900x600")
root.title("Youtube video downloader")
Label(root,text="Youtube video downloder",bg="black",fg="red",font=(None,20,"bold")).place(x=50,y=50,height=300,width=400)
Label(root,text="enter link here",font=(None,20,"bold"),bg="yellow",fg="black").place(x=600,y=50)

url_entry=Entry()
url_entry.place(x=600,y=100,height=30,width=200)
q=StringVar()
q.set("144p")
Options=["144p","240p","360p","480p","720p"]
my_menu=OptionMenu(root,q,*Options).place(x=600,y=150)
B1=Button(root,text="Download",command=yt,bg="blue",fg="red",font=(None,10,"bold")).place(x=600,y=200,height=50,width=100)





root.mainloop()
