from turtle import Turtle, Screen

arrow1 = Turtle ("arrow")
arrow2 = Turtle ("arrow")
arrow1.pencolor("red")
arrow2.pencolor("green")
arrow1.circle(20)

for x in range(30, 80, 10): #30 = velikost, 80, 10 = počet opakování
    arrow2.circle(x)



my_screen = Screen()
my_screen.exitonclick()