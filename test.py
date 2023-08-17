import turtle
turtle.left(90)
turtle.forward(30)
turtle.right(90)
for i in range(360):
    turtle.forward(0.5)
    turtle.right(1)

for i in range(24):
    for j in range(15):
        turtle.forward(0.5)
        turtle.right(1)
    turtle.left(90)
    turtle.forward(30)
    turtle.backward(30)
    turtle.right(90)

