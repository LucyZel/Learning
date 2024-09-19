from turtle import Turtle, Screen
import random

tommy = Turtle()
tommy.shape("turtle")
tommy.pensize(2)

colors = ["azure2", "brown4", "chartreuse",
"coral1", "cornsilk2", "DarkMagenta",
"DarkSeaGreen3", "DeepSkyBlue4"]
moves = 3

while moves != 9:
    random_color = random.choice(colors)
    tommy.pencolor(random_color)
    for _ in range(moves):
        tommy.forward(100)
        tommy.right(360/moves)
    
    moves += 1

# for _ in range(3):
#     tommy.forward(100)
#     tommy.right(120)
    
# for _ in range(4):
#     tommy.forward(100)
#     tommy.right(90)
    
# for _ in range(5):
#     tommy.forward(100)
#     tommy.right(72)  


my_screen = Screen()
my_screen.exitonclick()
