#testovací soubor
from turtle import Turtle, Screen
import time

my_screen = Screen()
my_screen.bgcolor("green")
my_screen.title("Vítejte ve hře Snake")
my_screen.setup(width=600, height=600)
my_screen.tracer(False) #zamrzne se, řídíme sami, kdy se má screen načíst


square1 = Turtle("square")
square1.penup()
square1.goto(0, 0)
square2 = Turtle("square")
square2.penup()
square2.goto(-20, 0)


for _ in range(80):
    square1.forward(10)
    square2.forward(10)
    time.sleep(1)
    my_screen.update()
    

my_screen.exitonclick()