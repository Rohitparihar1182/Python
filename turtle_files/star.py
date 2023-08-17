
"""
Created on Fri Jan 15 08:44:17 2021

@author: Rohit
"""
import turtle
turtle.right(36)

for i in range(3):
    
    if i==0:
        turtle.color("red")
    elif i==1:
        turtle.color("blue")
    else:
        turtle.color("green")
    turtle.begin_fill()
    for j in range(5):
        turtle.forward(200)
        turtle.left(180-36)
    if i==0:
        turtle.right(180-36)
    elif i==1:
        turtle.right(90+18)
        
    turtle.end_fill()



turtle.hideturtle()
