from tkinter import *
#from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("Clock")
def time():
    real_time=strftime("%H:%M:%S %p")
    Time.config(text=real_time)
    Time.after(1000,time)

Time=Label(root,font="DS-DIGIT 40",foreground="cyan",background="black")
Time.pack(anchor=CENTER)

time()
mainloop()