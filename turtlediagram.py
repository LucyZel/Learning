from turtle import Turtle, Screen

colors = ["violet", "yellow", "red", "green", "blue", "pink"]

arrow = Turtle("arrow")

for x in range(100):
    arrow.pencolor(colors[x%6])
    arrow.forward(x)
    arrow.left(60)



screen = Screen()
screen.exitonclick()