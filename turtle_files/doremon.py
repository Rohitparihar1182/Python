from turtle import *
speed(0)
#left(90)
color("blue")
begin_fill()
circle(80)
end_fill()
color("white")
begin_fill()
circle(55)
end_fill()
circle(55,180)
right(90)
for i in range(2):
    begin_fill()
    circle(20)
    end_fill()
    color("black")
    circle(20)
    right(180)
    color("white")

right(90)
for i in range(2):
    forward(12)
    right(90)
    color("black")
    begin_fill()
    circle(5)
    end_fill()
    left(90)
    forward(2)
    right(90)
    color("white")
    begin_fill()
    circle(2.5)
    end_fill()
    if i==0:
        right(90)
        forward(15)
    
    end_fill()
right(90)
goto(0,80)
right(90)
forward(10)
left(90)
color("red")
begin_fill()
circle(10)
end_fill()
right(90)
color("black")
forward(45)
left(90)
for i in range(30):
    forward(1)
    left(1)
right(180)
for i in range(60):
    forward(1)
    right(1)
color("white")
goto(0,3)
color("red")
left(30)
begin_fill()
fd(75)
left(90)
fd(15)
left(90)
fd(150)
left(90)
fd(15)
end_fill()
left(90)
fd(75)
left(90)
fd(15)
right(45)
#for i in range()
