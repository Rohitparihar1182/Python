from tkinter import *
root=Tk()
root.geometry("600x600")
root.title("Spin boxes")

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
day=StringVar()

spin_box=Spinbox(root,from_=1,to=20,increment=1,textvariable=day).pack()
root.mainloop()
