from turtle import Turtle, Screen, right
import random
window = Screen()
tur = Turtle()
window.colormode(255)
z = 0
p = 0
po = -200
tur.home()
tur.penup()
tur.setpos(-500, -250 )
for y in range(1, 11):
    if z==0:
        for x in range(1,11):
            r = random.randint(1, 255)
            g = random.randint(1, 255)
            b = random.randint(1, 255)
            tup = (r, g, b)
            tur.pencolor(tup)
            tur.dot(20, (tup))
            tur.forward(50)
            z +=1
            p  = 50  
    else:
        tur.home()
        tur.setpos(-500, po)
        for x in range(1,11):
            r = random.randint(1, 255)
            g = random.randint(1, 255)
            b = random.randint(1, 255)
            tup = (r, g, b)
            tur.pencolor(tup)
            tur.dot(20, (tup))
            tur.forward(50)
        po = po+50

