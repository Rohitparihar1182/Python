import tkinter as tk
button = {}

def toggle_text(button_number):
    print(button_number)

    if (button[button_number][1] == "On"):
        button[button_number][0].configure(text = "Coil %d is Off")
        button[button_number][1]='Off'
    else:         
        button[button_number][0].configure(text = "Coil %d is On")
        button[button_number][1]='On'


root = tk.Tk()
root.title("Click the Buttons to change the state of the coil")

for i in range(1,13):
    button[i]  = [tk.Button(text="Coil %d is On"  , 
                           width=50, 
                           command=lambda i=i: toggle_text(i)), "On"]
    button[i][0].grid(row = i, column = 1)


root.mainloop()
