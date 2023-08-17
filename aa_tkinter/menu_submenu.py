from tkinter import *
#creating function for my menus
def new():
    print("this will open a new file")
def open():
    print("this will open an exisitng file")
def save():
    print("this will save the program")
def saveas():
    print("this will save as you want to save")
root=Tk()
root.geometry("800x600")
root.title("IDLE")
#creating menu
rohit=Menu(root)
root.config(menu=rohit)
#creating sub menus
rohit1=Menu(rohit,tearoff=0)
rohit1.add_command(label="new file",command=new)
rohit1.add_command(label="open",command=open)
rohit1.add_command(label="save",command=save)
rohit1.add_command(label="saveas",command=saveas)
rohit1.add_separator()

rohit1.add_command(label="exit",command=quit)
#packing our menu

#adding sub menus
rohit.add_cascade(label="File",menu=rohit1)



root.mainloop()
