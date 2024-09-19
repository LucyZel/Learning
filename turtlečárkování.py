from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")

for _ in range (6):
    tommy.pendown()
    tommy.forward(25)
    tommy.penup()
    tommy.forward(25)


my_screen = Screen()
my_screen.exitonclick()