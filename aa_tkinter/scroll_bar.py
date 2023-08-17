from tkinter import *

root=Tk()
root.geometry("600x600")
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
text=Text(root,yscrollcommand=scroll.set)
text.pack(fill=BOTH)
scroll.config(command=text.yview)


root.mainloop()
