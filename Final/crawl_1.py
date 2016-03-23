from turtle import *
import random
count = 1
penup()
goto(-100,-100)
pendown()
goto(100, - 100)
goto(100, 100)
goto(-100, 100)
goto(-100, -100)
penup()
goto(0,0)
pendown()
while True:
    if count < 6:
        color("red")
    elif 5 < count < 11:
        color("green")
    elif 10 < count < 16:
        color("blue")
    elif 15 < count < 21:
        color("yellow")
    elif 20 < count < 26:
        color("cyan")
    elif 25 < count < 31:
        color("magenta")
    degree = random.randint(0,359)
    straight = random.randint(1, 100)
    left(degree)
    forward(straight)
    count += 1
    if 97 < abs(xcor()) < 102:
        break
    elif 97 < abs(ycor()) < 102:
        break
    if abs(ycor()) > 100 or abs(xcor()) > 100:      
        penup()
        goto(0,0)
        pendown()
done()
