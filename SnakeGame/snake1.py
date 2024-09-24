from turtle import Turtle, Screen
import time
import random

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
head.direction = "stop"

#jablko
apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

#tělo
body_parts = []

#funkce
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
def move_up():
    head.direction = "up"
    
def move_down():
    head.direction = "down"

def move_right():
    head.direction = "right"
    
def move_left():
    head.direction = "left"
    
#kliknutí na klávesy
my_screen.listen()
my_screen.onkeypress(move_up, "w")
my_screen.onkeypress(move_down, "s")
my_screen.onkeypress(move_right, "d")
my_screen.onkeypress(move_left, "a")
    
#hlavní cyklus
while True:
   
    #kolize hada s obrazovkou
    if head.xcor() > 290 or head.xcor() < - 290 or head.ycor() < 290 or head.ycor() < - 290:
        time.sleep(2)
        head.goto(0, 0)
        head.direction == "stop"
        
        #skryjeme části těla
        for one_body_part in body_parts:
            one_body_part.goto(1000, 1000)
            
        #vyprázdníme list s částmi těla
        body_parts.clear()
    
    
    if head.distance(apple) < 20:
        x = random.randint (-280, 280)
        y = random.randint (-280, 280)
        apple.goto(x, y)
        
        #přidání části těla
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)
        
    for index in range(len(body_parts) -1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)    
    
    
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)
     
    move()   
    
    my_screen.update()
    
    time.sleep(0.1)


my_screen.exitonclick()