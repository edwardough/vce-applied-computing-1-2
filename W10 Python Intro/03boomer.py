print("Welcome to the generation generator")
flag = True
while flag == True:
    try:
        dob = int(input("Enter your year of birth: "))
        flag = False
    except: # catches ValueErrors in case user typed in a non-numeric value
        print("An error has occured, try again next time with a number only.")

generation = None # declaring a variable but not assigning anything to it with 'None'

if dob <= 1945:
    generation = "Silent"
elif dob <= 1964: # elif ensures that not every statement is evaluated.
    generation = "Baby Boomer"
elif dob <= 1980:
    generation = "GenX"
elif dob <= 1995:
    generation = "Millenial"
else:
    generation = "iGen"

print("Your generation is:", generation)