from turtle import Turtle, Screen
import time
import random

# proměnné
score = 0
highest_score = 0

my_screen = Screen()
my_screen.bgcolor("green")
my_screen.title("Vítejte ve hře Snake")
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

# hadí hlava
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# jablko
apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

# skóre
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write("Skóre: 0 Nejvyšší skóre: 0", align="center", font=("Arial", 18))

# tělo
body_parts = []

# funkce
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
    if head.direction != "down":
        head.direction = "up"
    
def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_right():
    if head.direction != "left":
        head.direction = "right"
    
def move_left():
    if head.direction != "right":
        head.direction = "left"
    
# kliknutí na klávesy
my_screen.listen()
my_screen.onkeypress(move_up, "w")
my_screen.onkeypress(move_down, "s")
my_screen.onkeypress(move_right, "d")
my_screen.onkeypress(move_left, "a")
    
# hlavní cyklus
def game_loop():
    global score, highest_score

    # Kontrola kolize se zdí
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
            
        # Skrytí částí těla
        for part in body_parts:
            part.goto(1000, 1000)
                
        # Vyprázdnění seznamu
        body_parts.clear()
            
        # Reset skóre
        score = 0
        score_sign.clear()
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18))
        
    # Kontrola kolize s jablkem
    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)
            
        # Přidání části těla
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)
            
        # Zvýšení skóre
        score += 10
            
        if score > highest_score:
            highest_score = score
                
        score_sign.clear()    
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18))
            
    # Pohyb částí těla
    for index in range(len(body_parts) - 1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)    
        
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)
        
    move()
        
    # Kontrola kolize s tělem
    for part in body_parts:
        if part.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"  
                
            # Skrytí částí těla
            for part in body_parts:
                part.goto(1000, 1000)
                
            # Vyprázdnění seznamu
            body_parts.clear()
                
            # Reset skóre
            score = 0
            score_sign.clear()
            score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18))
        
    my_screen.update()
    my_screen.ontimer(game_loop, 100)  # Nastavení intervalu pro hladší aktualizace

# Spuštění herního cyklu
game_loop()  

my_screen.exitonclick()