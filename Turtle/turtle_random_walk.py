from turtle import Turtle, Screen, right, window_width
import random
window = Screen()
tur = Turtle()
window.setworldcoordinates(-500, -500, 500, 500)
tur.speed("fastest")
tur.pensize("9.999999999")

window.colormode(255)
window.bgcolor("black")
window.exitonclick
width, height = 800, 600

def rightt():
    tur.right(90)
    tur.forward(random.randint(1,101))
    x, y = tur.position()

    if -width < x < width and -height < y < height:
        return
    else:
        tur.undo()

def leftt():
    tur.left(90)
    tur.forward(random.randint(1,101))
    x, y = tur.position()

    if -width < x < width and -height < y < height:
        return

    tur.undo()

def straight():
    tur.forward(random.randint(1,101))
    x, y = tur.position()

    if -width < x < width and -height < y < height:
        return

    tur.undo()




for x in range(1, 10000000):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tup = (r, g, b)
    tur.pencolor(tup)
    tur.speed("fastest")


    m=random.randint(1,3)
    if m == 1:
        rightt()
    elif m==2:
        leftt()
    else:
        straight()


