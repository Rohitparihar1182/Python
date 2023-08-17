import turtle
turtle.speed(50)


turtle.begin_fill()
turtle.color("red")
for i in range(360):
    turtle.right(1)
    turtle.forward(1)
turtle.end_fill()

turtle.begin_fill()
turtle.color("blue")    
for i in range(360):
    turtle.left(1)
    turtle.forward(1)
turtle.end_fill()
turtle.hideturtle()

        
