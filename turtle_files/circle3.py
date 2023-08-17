from turtle import *
bgcolor("black")
colours=["green","red","cyan","magenta","blue","yellow"]
width(2)
speed(0)
for i in range(6):
    for colour in colours:
        color(colour)
        circle(100)
        left(10)
hideturtle()
