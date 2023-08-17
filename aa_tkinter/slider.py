from tkinter import *
def hey():
    print("total amount=",slider.get())
root=Tk()
root.geometry("600x600")
slider=Scale(root,width=15,length=300,from_=0,to=100,tickinterval=20,orient=HORIZONTAL)
slider.pack()
#slider.set(3)
#slider2=Scale(root,width=15,length=300,from_=0,to=100).pack()
Button(root,text="submit",command=hey).pack()



root.mainloop()
