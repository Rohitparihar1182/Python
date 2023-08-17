from tkinter import *
import tkinter.messagebox as tmsg
def Open():
    pass
def New():
    pass
def copy():
    pass
def submit():
    with open("bio.txt","w") as f:
        f.write(text.get("1.0","end-1c"))
root=Tk()
root.geometry("600x600")
main_menu=Menu(root)
file=Menu(main_menu,tearoff=0)
file.add_command(label="Open",command=Open)
file.add_command(label="new",command=New)
file.add_command(label="save",command=submit)
root.config(menu=main_menu)
main_menu.add_cascade(label="File",menu=file)
edit=Menu(root,tearoff=0)
edit.add_command(label="copy",command=copy)
main_menu.add_cascade(label="Edit",menu=edit)


text=Text(root)
text.pack(fill=Y)

root.mainloop()

