from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("590x590")

image=Image.open("rohit.jpg")
photo=ImageTk.PhotoImage(image)

label=Label(image=photo)
label.pack()

root.mainloop()
