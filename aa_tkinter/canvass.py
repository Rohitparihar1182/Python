from tkinter import *
root=Tk()
canvas_width=800
canvas_height=800
root.geometry("800x800")
root.title("Welcome to my canvas gui")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()
can_widget.create_line(0,0,400,400,fill="red")
can_widget.create_line(0,400,400,0,fill="blue")
can_widget.create_rectangle(200,200,400,400,fill="black")
can_widget.create_oval(0,0,225,225,fill="grey")
