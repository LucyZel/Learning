from turtle import Turtle, Screen

my_screen = Screen()
tommy = Turtle("turtle")

def move_forward():
    tommy.forward(20)
    
#stisknutí klávesy
my_screen.listen()
my_screen.onkeypress(move_forward, "w")

my_screen.exitonclick()