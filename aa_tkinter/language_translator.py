from tkinter import *
from translate import Translator
def func():
    translator=Translator(from_lang="lang1.get()",to_lang="lang2.get()")
    translated=translator.translate(str1.get())
    str2.set(translated)
    print(str2)
root=Tk()
root.geometry("900x600")
root.title("language translator")
Label(root,text="Text Translator",fg="green",bg="yellow",font=("arial",30,"bold")).place(x=200,y=10)

lang1=StringVar()
lang2=StringVar()
lang1.set("English")
lang2.set("Hindi")
languages=["Hindi","English","Spanish","German"]
l1=OptionMenu(root,lang1,*languages)
l1.place(x=100,y=100)

l2=OptionMenu(root,lang2,*languages)
l2.place(x=350,y=100)

str1=StringVar()
str2=StringVar()
E1=Entry(root,textvariable=str1)
E1.place(x=100,y=200)

E2=Entry(root,textvariable=str2,width=100)
E2.place(x=350,y=200)

B1=Button(root,text="Translate",fg="green",bg="yellow",font=("arial",30,"bold"),command=func)
B1.place(x=225,y=300)

root.mainloop()
