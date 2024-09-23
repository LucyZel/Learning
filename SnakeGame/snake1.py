from turtle import Turtle, Screen
import time

my_screen = Screen()
my_screen.bgcolor("green")
my_screen.title("Vítejte ve hře Snake")
my_screen.setup(width=600, height=600)
my_screen.tracer(False)

#hadí hlava
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "up"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

while True:
    move()
    time.sleep(0.1)
    my_screen.update()


my_screen.exitonclick()