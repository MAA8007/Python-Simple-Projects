from turtle import Turtle, Screen, right
import random
window = Screen()
tur = Turtle()
window.colormode(255)
tur.home()



def forw():
    tur.forward(100)

def leftt():
    tur.left(10)


def rightt():
    tur.right(10)


def back():
    tur.backward(100)



window.onkey(forw, "w")
window.onkey(leftt, "a")
window.onkey(rightt, "d")
window.onkey(back, "s")
window.listen()
window.exitonclick()

