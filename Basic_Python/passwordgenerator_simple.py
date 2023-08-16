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
nr_letters= int(input("How many characters would you like in your password? (Including numbers and symbols) \n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for y in range(nr_symbols+1):
    sym.append(symbols[y])

for z in range(nr_numbers+1):
    nums.append(numbers[z])

lets = nr_letters-(nr_symbols+nr_numbers)
for x in range(lets+1):
    le.append(letters[x])

ps = le + sym + nums 
string = "".join(ps)
print(string) 
