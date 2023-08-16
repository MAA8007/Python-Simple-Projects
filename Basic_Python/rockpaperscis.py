
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
pcc = 0
playerc = 0
counter = 1 
import random
num = random.randint(1, 3)
while counter <4:
    inp = input("enter")

    if inp == "rock":
        print("player", rock)
    elif inp == "scissors":
        print("player", scissors)
    elif inp == "paper":
        print("player", paper)

    if num == 1:
        pc = "rock"
        print("PC", rock)
    elif num ==2:
        pc = "paper"
        print("PC", paper)
    elif num == 3:
        pc = "scissors"
        print("PC", scissors)

    if inp == pc:
        print("draw")
    elif inp == "rock" and pc =="paper":
        print("pc won")
        pcc = pcc +1
    elif inp == "paper" and pc =="rock":
        print("player won")
        playerc = playerc +1
    elif inp == "scissors" and pc =="paper":
        print("player won")
        playerc = playerc +1
    elif inp == "paper" and pc =="scissors":
        print("pc won")
        pcc = pcc +1 
    elif inp == "rock" and pc =="scissoes":
        print("player won")
        playerc = playerc +1
    elif inp == "scissors" and pc =="rock":
        print("pc won")
        pcc = pcc +1
    counter += 1 
if pcc> playerc:
    print("PC won")
if  playerc> pcc:
    print("player won")







