from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")
tommy.color("red")
tommy.begin_fill()


# tommy.forward(60)
# tommy.right(90)
# tommy.forward(60)
# tommy.right(90)
# tommy.forward(60)
# tommy.right(90)
# tommy.forward(60)
# tommy.right(90)

for _ in range(0, 4):
    tommy.forward(60)
    tommy.right(90)
    
tommy.end_fill()


my_screen = Screen()
my_screen.exitonclick()