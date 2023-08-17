import turtle
sc=turtle.Screen()
sc.setup(600,600)
spiral=turtle.Turtle()
spiral.speed(10)
sc.bgcolor("black")
col=['yellow','blue','white','green','red']
c=0
for i in range(50):
    if c<4:
        c+=1
    else:
        c=0
    spiral.color(col[c])
    spiral.forward(i*10)
    spiral.right(144)
    
turtle.hideturtle()

