import turtle

colour=["yellow","green","red","blue","orange","pink"]
for i in range(120):
    turtle.color(colour[i%6])
    turtle.width(i/5+1)
    turtle.forward(i)
    turtle.left(20)

