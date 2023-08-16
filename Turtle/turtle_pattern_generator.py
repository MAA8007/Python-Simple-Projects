from turtle import Turtle, Screen
import random
colors = ["brown", "red", "yellow", "green", "blue", "black"]

tur = Turtle()
tur.speed("fastest")
tur.pensize(9)
r = 50
h = int(r/2)
for x in range(3, h+1):
    r = random.choice(colors)
    tur.pencolor(r)
    for y in range(1, x+1):
        tur.forward(50)
        tur.right(360/x)


for x in range(1,h+1):
    r = random.choice(colors)
    tur.pencolor(r)
    for y in range(1, x+1):
        tur.forward(50)
        tur.left(360/x)
    
    
        
