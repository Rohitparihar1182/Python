import os
from tkinter import *
from tkinter import Text, filedialog

apps=[]#263D41

def addApp():
    filename=filedialog.askopenfilename(initialdir="/",title="Select file",
        filetypes=(("executable",".exe"),("all files","*.*")))
    apps.append(filename)
    #print(filename)
    for widget in frame.winfo_children():
        widget.destroy()
    for app in apps:
        label=Label(frame,text=app,fg="gray")
        label.pack()

def runApp():
    for app in apps:
        os.startfile(app)

root=Tk()
canvas=Canvas(root,height=550,width=600,bg="#263D41")
canvas.pack()

frame=Frame(root,bg="white")
frame.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)

openfile=Button(root,text="OpenFile",padx=10,pady=5,fg="white",bg="",command=addApp)
openfile.pack()

runapp=Button(root,text="RunApp",padx=10,pady=5,fg="white",bg="#263D41",command=runApp)
runapp.pack()

root.mainloop()
