import random

while True:
    try:
        level= int(input("level: "))
        while level<0:
            level= int(input("level: "))
        break
    except ValueError as e:
        level = print("Invalid input. Try again...")



num= random.randint(1, level)
while True:
    try:
        guess= int(input("guess: "))
        while guess<0:
            guess= int(input("level: "))
        break
    except ValueError as e:
        level = print("invalid input. Try again...")


while guess!=num:
    if guess>num:
        guess= int(input('Too large! '))
    elif guess<num:
        guess= int(input('Too large! '))

print("just right!")


