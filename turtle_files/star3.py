import turtle

screen=turtle.Screen()
screen.setup(900,700)
screen.title("Stars")
screen.bgcolor("black")

star=turtle.Turtle()
star.forward(90)
star.speed(0)
star.color("yellow")
star.width(2)
def func():
    for i in range(5):
        star.forward(50)
        for j in range(5):
            star.forward(20)
            star.left(180-36)
        star.left(180-36)
for i in range(5):
    func()
    star.right(180-36)
    star.forward(200)

x=True
while x:
    if turtle.Terminator():
        x=False