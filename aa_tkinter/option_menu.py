from tkinter import *
root=Tk()
root.geometry("600x600")
root.title("Option menu")

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
day=StringVar()
day.set(days[1])
option_menu=OptionMenu(root,day,*days).pack()


root.mainloop()
