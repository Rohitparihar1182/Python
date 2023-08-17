from tkinter import *
import tkinter.messagebox as tmsg
my_idle=Tk()
def func():
    print("OOPS!!!!")
def rate():
    review=tmsg.askquestion("Kindly give a review","did you have a great experience")
    if review=="yes":
        msg="Great,kindly rate us in app store"
        
    else:
        msg="Tell us what went wrong we'll try to figure it out"
    tmsg.showinfo("Review",msg)

w=600
h=800
my_idle.geometry(f"{h}x{w}")
my_idle.title("Python 3.9.0 ")

#declaring main
file=Menu(my_idle)
#declaring sub menus
sub_file=Menu(file,tearoff=0)
sub_edit=Menu(file,tearoff=0)
sub_Format=Menu(file,tearoff=0)
sub_run=Menu(file,tearoff=0)
sub_rate=Menu(file,tearoff=0)
#declaring commands
#for file menu
sub_file.add_command(label="new file",command=func)
sub_file.add_command(label="open",command=func)
sub_file.add_command(label="save",command=func)
sub_file.add_command(label="exit",command=func)
#for edit menu
sub_edit.add_command(label="undo",command=func)
sub_edit.add_command(label="cut",command=func)
sub_edit.add_command(label="copy",command=func)
sub_edit.add_command(label="paste",command=func)
#for format menu
sub_Format.add_command(label="format paragraph",command=func)
sub_Format.add_command(label="indent region",command=func)
sub_Format.add_command(label="dedent region",command=func)
sub_Format.add_command(label="comment out region",command=func)
#for run menu
sub_run.add_command(label="Run module",command=func)
sub_run.add_command(label="Run and customize",command=func)
sub_run.add_command(label="check module",command=func)
sub_run.add_command(label="python shell",command=func)
#for rate menu
sub_rate.add_command(label="Rate us",command=rate)
#packing main menu
my_idle.config(menu=file)

#packing sub menus
file.add_cascade(label="File",menu=sub_file)
file.add_cascade(label="Edit",menu=sub_edit)
file.add_cascade(label="Format",menu=sub_Format)
file.add_cascade(label="Run",menu=sub_run)
file.add_cascade(label="Rate",menu=sub_rate)
text=Text(my_idle).pack(fill=BOTH)
my_idle.mainloop()
