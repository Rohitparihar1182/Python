import turtle
col=["red","green","blue","black","yellow"]
a=[200,160,120,80,40]
for i in range(5):
    turtle.color(col[i])
    turtle.begin_fill()
    for j in range(4):
        
        turtle.forward(a[i])
        turtle.left(90)
    
    turtle.end_fill()
    
turtle.hideturtle()
