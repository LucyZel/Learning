from turtle import Turtle, Screen
import random
import turtle

#změna barevného módu
turtle.colormode(255)

#generování a základní nastavení
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(15)

#funkce na generování barvy
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return (colour)

#kruhy
def spirograph(gap):
    for number in range (int(360/gap)):
        tommy.pencolor(random_colour())
        tommy.circle(80)
        tommy.left(gap)
    
spirograph(10)


my_screen = Screen()
my_screen.exitonclick()