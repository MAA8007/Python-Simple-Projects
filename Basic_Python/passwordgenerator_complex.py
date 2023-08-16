#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
sym =[]
nums = []
le = []
ps = []
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many characters would you like in your password (Including numbers and symbols)? \n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



# the code below generates a random and harder to crack password

for y in range((nr_symbols)):
    num = random.randint(1, len(symbols))
    if num == len(symbols):
        num-=1
    sym.append(symbols[num])

for z in range((nr_numbers)):
    num = random.randint(1, len(numbers))
    if num == len(numbers):
        num-=1
    nums.append(numbers[num])

lets = nr_letters-(nr_symbols+nr_numbers)
for x in range(lets):
    num = random.randint(1, len(letters))
    if num == len(letters):
        num-=1
    le.append(letters[num])

randorder = random.randint(0, 5)
ps = le + sym + nums 
for x in range(100001):
    random.shuffle(ps)
final_password = "".join(ps)
print(final_password) #generated password

import bcrypt
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(final_password.encode('utf-8'), salt) #encrypted password
print(hashed)



