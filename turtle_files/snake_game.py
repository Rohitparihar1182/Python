import turtle
import random
import time

HEIGHT,WIDTH=500,500

def init_turtle():
    screen=turtle.Screen()
    screen.setup(HEIGHT,WIDTH)
    screen.title("Snake Game")
    screen.bgcolor("blue")

def main():
    snake=turtle.Turtle()
    snake.shape("square")
    snake.color("green")
    snake.width(2)

def food():
    food=turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    x,y=random.randint(-((WIDTH/2)-20),((WIDTH/2)-20)),random.randint(-((HEIGHT/2)-20),((HEIGHT/2)-20))
    food.setpos(x,y)


init_turtle()
main()
time.sleep(3)
food()
time.sleep(5)
