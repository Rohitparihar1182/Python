from tkinter import *
x=[]
o=[]
turn=1

def click(a):
    
    global x,o,turn
    
    if turn==1:
        if a==1:
            button1.configure(text="X",font=("lucida",30,"bold"),fg="yellow")
            #turn+=1
        elif a==2:
            button2.configure(text="X",font=("lucida",30,"bold"))
            #turn+=1
        
def btns():
    button1=Button(root,text="",height=10,width=20,command=lambda i=1:click(i))
    button1.grid(row=1,column=1)    
    button2=Button(root,text="",height=10,width=20,command=lambda i=2:click(i))
    button2.grid(row=1,column=2)
    button3=Button(root,text="",height=10,width=20,command=lambda i=3:click(i))
    button3.grid(row=1,column=3)
    button4=Button(root,text="",height=10,width=20,command=lambda i=4:click(i))
    button4.grid(row=2,column=1)
    button5=Button(root,text="",height=10,width=20,command=lambda i=5:click(i))
    button5.grid(row=2,column=2)
    button6=Button(root,text="",height=10,width=20,command=lambda i=6:click(i))
    button6.grid(row=2,column=3)
    button7=Button(root,text="",height=10,width=20,command=lambda i=7:click(i))
    button7.grid(row=3,column=1)
    button8=Button(root,text="",height=10,width=20,command=lambda i=8:click(i))
    button8.grid(row=3,column=2)
    button9=Button(root,text="",height=10,width=20,command=lambda i=9:click(i))
    button9.grid(row=3,column=3)

root=Tk()
root.geometry("700x540")
#root.configure(bg="pink")
btns()
                          
root.mainloop()
