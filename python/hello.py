import math
import random

'''

#basic python

result = 3/4
print(3 / 4.0)
print(result)

name = raw_input("Pls enter name: ")
print(name+" is cool")

# number guesser

guess1 = raw_input("Pls enter a number from 1-69420: ")
guess = int(guess1,10)
if guess == 42069:
    print("wow you amazing")
elif guess > 42069:
    print("too high lmao")
else:
    print("u suck lmao")

# your age

ageyears = raw_input("Pls enter age: ")
ageyears = int(ageyears,10)
ageseconds = ageyears*365*24*3600
ageseconds = str(ageseconds)
year = 2019-ageyears
year = str(year)
print("You have lived for "+ageseconds+" seconds. You were born in "+year)

# pass or fail

quiz = raw_input("Quiz score: ")
proj = raw_input("Project score: ")
final = raw_input("Final score: ")

final = int(final,10)

proj = int(proj)
quiz = int(quiz)

avg = proj+quiz+final
avg = avg/3

print(avg)

if final < 60:
    print("You fail cos your final suck")
elif avg < 60:
    print("You fail cos average suck")
elif avg < 70:
    print("You got D")
elif avg < 80:
    print("You got C")
elif avg < 90:
    print("You got B")
elif avg > 89:
    print("You got an A!!!!")


# hello world but better

message = "Hello world I am see tow"
length = len(message)
index = range(length)

for idx in index:
    print(message[idx])


# some encryption thing WITH ERROR CHECKING!!

message = raw_input("Message to encrypt: ")
key = raw_input("Private key: ")
key = int(key)



output = ""
for char in message:
    if key > 260000:
        print("You suck. Use a smaller private key value.")
    else:
        char = ord(char)
        char = char+key
        while char > 122:
            char = char-26
        char = chr(char)
        output = output+char

print(output)


# number guesser 2.0

done = False

while not done:
    guess1 = raw_input("Pls enter a number from 1-69420: ")
    guess = int(guess1,10)
    if guess == 42069:
        print("wow you amazing")
        done = True
    elif guess > 42069:
        print("too high lmao")
    else:
        print("u suck lmao")

'''

# encryption 2.0 w ERROR CHECKING!!

done = False

while not done:
    choice = raw_input("\n=================\nType e to encrypt\nType d to decrypt\nType q to quit\n=================\nYour choice: ")

    if choice=="e":
        message = raw_input("Message to encrypt: ")
        key = raw_input("Private key: ")
        key = int(key)



        output = ""
        for char in message:
            if key > 260000:
                print("You suck. Use a smaller private key value.")
            else:
                char = ord(char)
                char = char+key
                while char > 122:
                    char = char-26
                char = chr(char)
                output = output+char

        print("Your encrypted string is "+output)

    elif choice=="d":
        message = raw_input("Message to decrypt: ")
        key = raw_input("Private key: ")
        key = int(key)



        output = ""
        for char in message:
            if key > 260000:
                print("You suck. Use a smaller private key value.")
            else:
                char = ord(char)
                char = char-key
                while char < 97:
                    char = char+26
                char = chr(char)
                output = output+char

        print("Your decrypted string is "+output)
    elif choice=="q":
        done = True
        print("Byebye")
    else:
        print("")

'''

# Functions

def printmenu():
    menu = """
    =================
    type e to encrypt
    type d to decrypt
    type q to quit
    =================
    """
    print(menu)

def intinput(prompt):
    user_input = raw_input(prompt)
    return int(user_input)

def cipher(message, mode, key)

'''
