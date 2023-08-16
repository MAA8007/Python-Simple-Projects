alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
newalphs = []
store = ""
design = logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(design)



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if shift > 26:
    shift = shift % 26

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    

def caesar(direction, text, shift):
    if direction == "encode":
        for x in text:
            if x in alphabet:
                ind = alphabet.index(x)
                newind = ind + shift
                newalph = alphabet[newind]
                newalphs.append(newalph)
                str1 = ''.join(str(e) for e in newalphs)
            else:
                str1 += x
        print(str1)
    else:
        for x in text:
            ind = alphabet.index(x)
            newind = ind - shift
            newalph = alphabet[newind]
            newalphs.append(newalph)
        str2 = ''.join(str(e) for e in newalphs)
        print(str2)


caesar(direction, text, shift)

decide = input("Would you like to do it again?")
if decide == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)