import turtle
turtle.bgcolor("black")
turtle.color("red")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.color("blue")
turtle.begin_fill()
for i in range(4):
    turtle.right(90)
    turtle.forward(100)
turtle.end_fill()
turtle.color("yellow")
turtle.begin_fill()
for i in range(4):
    turtle.left(90)
    turtle.forward(100)
turtle.end_fil1()
turtle.right(90)
turtle.color("green")
turtle.begin_fill()
for i in range(4):
    turtle.left(90)
    turtle.forward(100)
turtle.end_fil1()


turtle.hideturtle()
