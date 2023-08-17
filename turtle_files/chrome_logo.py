from turtle import *
speed(0)
title("Chrome Logov")
color("red")
begin_fill()
left(90)
for i in range(120):
    forward(1)
    right(1)
forward(97.5)
left(120)
for i in range(120):
    forward(2)
    left(1)
left(60)
forward(97.5)
end_fill()
color("green")
backward(97.5)
begin_fill()
right(60)
for i in range(120):
    forward(2)
    left(1)
left(60-1)
forward(100)
left(180)
for i in range(120):
    forward(1)
    right(1)
end_fill()
for i in range(120-1):
    backward(1)
    left(1)
forward(98)
left(122)
color("yellow")
begin_fill()
for i in range(120):
    forward(2)
    left(1)
left(61)
forward(90)
left(171)
for i in range(110):
    forward(1)
    right(1)
end_fill()
color("white")
goto(5,-2)
right(120)
color("blue")

begin_fill()
for i in range(360):
    forward(0.9)
    right(1)
end_fill()

    
hideturtle()
