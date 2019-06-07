import random

guess1 = raw_input("1 - Scissors\n2 - Paper\n3 - Stone\nEnter your choice: ")
value2 = random.randint(1, 3)
value1 = int(value1)

states = {
  1: "Scissors",
  2: "Paper",
  3: "Stone"
}

# Print user and computer choice

print("You picked "+states[value1])
print("The computer picked "+states[value2])

if guess1 == guess2:
    print("It's a draw!")
elif value1 == 1 and value2 == 2 or value1 == 2 and value2 == 3 or value1 == 3 and value2 = 1:
    print("You win!")
else:
    print("You lost, sorry.")
