from tkinter import *
def button(event):
    print("alright")
root=Tk()
root.geometry("600x600")

b1=Button(root,text="click karo")
b1.pack()

b1.bind("<Button-1>",button)

root.mainloop()
