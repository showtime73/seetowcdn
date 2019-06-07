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

print(output)
