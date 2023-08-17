import turtle
turtle.color("white")
turtle.right(45)
turtle.goto(65,65)
turtle.color("blue")
for i in range(360):
    turtle.forward(1.62)
    turtle.right(1)
turtle.color("white")
turtle.goto(0,0)
turtle.left(45)


#outer circle
turtle.color("white")
turtle.goto(60,60)
turtle.right(45)
turtle.color("blue")

for i in range(360):
    turtle.forward(1.5)
    turtle.right(1)
turtle.right(90)
turtle.color("white")
turtle.goto(0,0)

#inner circle
turtle.forward(30)
turtle.right(90)
turtle.color("blue")
turtle.begin_fill()
for i in range(360):
    turtle.forward(0.5)
    turtle.right(1)
turtle.end_fill()
#lines
for i in range(24):
    for j in range(15):
        turtle.forward(0.5)
        turtle.right(1)
    turtle.left(90)
    turtle.forward(55)
    turtle.backward(55)
    turtle.right(90)
turtle.goto(0,0)
turtle.right(45)

#flag
turtle.goto(-30,0)
turtle.color("white")
turtle.goto(-400,90)
turtle.color("orange")
turtle.begin_fill()
turtle.forward(180)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(180)
turtle.right(90)
turtle.forward(800)
turtle.end_fill()
turtle.left(90)
turtle.color("white")
turtle.forward(180)
turtle.color("green")
turtle.begin_fill()
turtle.forward(180)
turtle.left(90)
turtle.forward(800)
turtle.left(90)
turtle.forward(180)
turtle.left(90)
turtle.forward(800)
turtle.end_fill()
turtle.hideturtle()



