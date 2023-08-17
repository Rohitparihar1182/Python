from tkinter import *
def add():
    global i
    i+=1
    lb.insert(END,i)
i=0
root=Tk()
root.geometry("600x600")
root.title("list box")
scroll=Scrollbar(root)
scroll.pack(fill=Y,side=RIGHT)
lb=Listbox(root,yscrollcommand=scroll.set)
lb.pack(fill=BOTH)
lb.insert(ACTIVE,"My numbers")
lb.insert(END,"0")
scroll.config(command=lb.yview)
Button(root,text="add numbers",command=add).pack()


root.mainloop()
