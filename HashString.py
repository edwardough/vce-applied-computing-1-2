def runHash( myList, myKey ):
    if len(myList) % 2 == 1:
        myList.append(" ") # If the list is odd in length add a blank space
    hashResult = [] # Create an empty list for the result
    # Loop through the list, grab each pair, operate on them, add the result to the list
    for i in range(0,len(myList)-1,2): # Note that i goes up by 2 but cannot be larger than length - 1
        # Note "&" is boolean AND "<<" shifts all the bits to the left "|" is boolean OR
        # They are bit level operations
        # ord converts the character to it's numeric equivalent on the ASCII table
        temp = (ord(myList[i]) & myKey) | ( (ord(myList[i+1]) << 3) & 255 )
        hashResult.append(temp)
   
    # print( "The numeric hash list is:", hashResult )

    strHash = ''
    for num in hashResult:
        # chr() converts a number into it's character equivalent on the ASCII table
        strHash += chr(num)

    print( "The string hash / signature is:", strHash )

while True:
    userInput = input("Enter a string for hashing or Q to quit: ")
    if userInput == 'Q':
        break
    else:
        userInput = list(userInput)
        pk = int(input("Enter a numeric password between 1 and 255: "))
        runHash( userInput, pk )

print("\nThanks for using HashString")

# TO DO
# The hash is only half the length of the input - for large inputs (eg "holyBible.txt") this is not a large enough reduction.
# So if the hashResult is of a certain length the process could be repeated until it is 8 characters long or something like that.
