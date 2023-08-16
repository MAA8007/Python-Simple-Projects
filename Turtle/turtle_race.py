from turtle import Turtle, Screen
import turtle
import random
raceon = True
screen = Screen()
screen.setup(500, 500)
tim = Turtle()
john = Turtle()
jeff = Turtle()
geoff = Turtle()
tim.shape("turtle")
john.shape("turtle")
jeff.shape("turtle")
geoff.shape("turtle")
tim.penup()
john.penup()
jeff.penup()    
geoff.penup()
predic = screen.textinput(title="enter", prompt="who do you think's gonna win?")
tim.color("red")
john.color("blue")
jeff.color("green")
geoff.color("yellow")

tim.goto(x= -230, y = 0)
john.goto(x= -230, y = 50)  
jeff.goto(x= -230,y = 100)
geoff.goto(x= -230,y= 150)

turts = [tim, john,jeff,geoff]
while raceon:
    turts[0].forward(random.randint(0, 20))
    turts[1].forward(random.randint(0, 20))
    turts[2].forward(random.randint(0, 20))
    turts[3].forward(random.randint(0, 20))
    if turts[0].xcor() > 500:
        raceon = False
        winner = tim
        print("The winner is tim")
    elif turts[1].xcor()>500:
        raceon = False
        winner = john
        print("The winner is john")
    elif turts[2].xcor()>500:
        raceon = False
        winner = jeff
        print("The winner is jeff")
    elif turts[3].xcor()>500:
        raceon = False
        winner = geoff
        print("The winner is geoff")

if predic== winner:
    print("congrats")
else:
    print("sorry")



screen.setup(500, 400)
screen.exitonclick()