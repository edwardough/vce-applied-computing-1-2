phobia = input("What's your phobia? ").lower() # lower() converts the input to lowercase
userInput = input("Text: ").lower()
replacement = "kitten"

if phobia[-1] == 's':
    replacement = "kittens"

if phobia in userInput:
    userInput = userInput.replace(phobia,replacement)
    print(userInput)
else:
    print("Phobia not found in text.")