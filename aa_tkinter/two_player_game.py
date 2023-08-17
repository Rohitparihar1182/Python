from tkinter import *
val=""
val1=""
a=2
turn=1
def game(event):
        global turn,options,val,val1
        if turn%2!=0:
                val=event.widget.cget("text")
                turn+=1
                
        else:
                val1=event.widget.cget("text")
                p2.set(val1)
                p2_entry.update()
                p1.set(val)
                p1_entry.update()
                turn+=1
                if p1==options[0]and p2==options[1]or p1==options[1]and p2==options[2]or p1==options[2]and p2==options[0]:
                        label=Label(root,text="Player1 wins",font=("lucida",30,"bold"),bg="black",fg="red").place(x=500,y=500)
                        s1.set(s1+1)
                        s1_entry.update()
                elif p1==options[1]and p2==options[0]or p1==options[2]and p2==options[1]or p1==options[0]and p2==options[2]:
                        label=Label(root,text="Player2 wins",font=("lucida",30,"bold"),bg="black",fg="red").place(x=500,y=500)
                        s2.set(s2+1)
                        s2_entry.update()
                elif p1==options[0]and p2==options[0]or p1==options[1]and p2==options[1]or p1==options[2]and p2==options[2]:
                        label=Label(root,text="lol!Tie...",font=("lucida",30,"bold"),bg="black",fg="red").place(x=500,y=500)
                else:
                        #error
                        pass
                
root=Tk()
root.geometry("1000x600")
root.title("2 Players Rock paper scissor")
root.configure(bg="yellow")
options=[" Rock  "," Paper ","Scissor"]
colours=["red","white","green"]
for i in range(3):
    B=Button(root,text=options[i],bg=colours[i],padx=60,pady=40,relief=SUNKEN)
    B.place(x=200,y=(100*i))
    B.bind("<Button-1>",game)


Label(root,text="Player 1",font=("arial",20)).place(x=10,y=10)
p1=StringVar()
p1.set("")
p1_entry=Entry(root,textvariable=p1,font=("arial",20))
p1_entry.place(x=10,y=50,height=30,width=100)
Label(root,text="Player 2",font=("arial",20)).place(x=450,y=10)
p2=StringVar()
p2.set("")
p2_entry=Entry(root,textvariable=p2,font=("arial",20))
p2_entry.place(x=450,y=50,height=30,width=100)



s1=IntVar()
s1.set(0)
s1_entry=Entry(root,textvariable=s1,font=("arial",20)).place(x=700,y=80,height=30,width=60)
s2=IntVar()
s2.set(0)
s2_entry=Entry(root,textvariable=s2,font=("arial",20)).place(x=760,y=80,height=30,width=60)

