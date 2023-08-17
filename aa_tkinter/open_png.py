from tkinter import *
from PIL import Image,ImageTk
rohit=Tk()
rohit.geometry("400x400")

#photo=PhotoImage(file="file_name")      this will used to read a png file
image=Image.open("image.jpg")
photo=ImageTk.PhotoImage(image)


#rohit_image=Label(image=photo).pack()


rohit.mainloop
