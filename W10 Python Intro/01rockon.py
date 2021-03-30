place = input("Where are you going? ")
desire = input("What do you want? ")
print("It's a long way to the",place,"if you wanna",desire)
# concatenation - great when you know you're dealing with strings
print("It's a long way to the " + str(place) + " if you wanna " + desire)
print("It's a long way to the %s if you wanna %s" % (place,desire))



