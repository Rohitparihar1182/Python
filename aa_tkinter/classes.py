from tkinter import *
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x700")
    def cmd(self):
        print("button clicked")
    def button(self):
        self.a=IntVar()
        self.a.set("a")
        self.b0=Button(root,text="1",activebackground="red",command=self.cmd,font=("arial",20),padx=10,relief=SUNKEN).grid(row=0,column=0)
        self.b1=Button(root,text="2",activebackground="red",command=self.cmd,font=("arial",20),padx=10,relief=SUNKEN).grid(row=0,column=1)
        self.b2=Button(root,text="3",activebackground="red",command=self.cmd,font=("arial",20),padx=10,relief=SUNKEN).grid(row=0,column=2)
if __name__=="__main__":
    root=GUI()
    root.button()
