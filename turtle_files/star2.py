import turtle
turtle.bgcolor("black")
col=["green","orange","red","blue","yellow","purple"]
c=0
turtle.speed(0)

for i in range(150):
    if c<5:
        c+=1
    else:
        c=0
    turtle.color(col[c])
    if i==150-1:
        turtle.forward(30)
    else:
        turtle.forward(i)
        turtle.left(59)
    
turtle.hideturtle()
