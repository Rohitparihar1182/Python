from tkinter import *
root=Tk()
root.geometry("800x400")
f1=Frame(root,bg="grey",borderwidth=6)
f1.pack(side=LEFT,fill=Y)
f2=Frame(root,bg="black",borderwidth=5)
f2.pack(side=TOP,fill=X)
l=Label(f1,text="Quick Access")
l.pack(side=TOP,padx=40,pady=175)
l1=Label(f2,text="Frequent folders",fg='red')
l1.pack(side=TOP,padx=200,pady=50)
root.mainloop()