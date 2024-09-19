from turtle import Turtle, Screen
import random
import turtle

#změna barevného módu
turtle.colormode(255)

tommy = Turtle()
tommy.shape("turtle")


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

#colors = ["azure2", "brown4", "chartreuse", "coral1", "cornsilk2", "DarkMagenta", "DarkSeaGreen3", "DeepSkyBlue4", "blue4"]
rotation = [0, 90, 180, 270]
speed = 1


for number in range(200):
    #výběr barvy
    tommy.pencolor(random_colour())
    
    #tloušťka čáry
    if number <= 10:
        tommy.pensize(number)

    #pohyb
    tommy.forward(30)
    tommy.right(random.choice(rotation))
    
    #vyšší rychlost
    tommy.speed(speed)
    speed += 1


my_screen = Screen()
my_screen.exitonclick()