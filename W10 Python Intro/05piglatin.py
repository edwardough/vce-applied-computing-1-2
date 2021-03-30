while True:
    word = input("Word, or 'Q' to quit > ")
    if word[-2:] == 'ay':
        word = word[0:-2] # removes the final two characters
        result = word[-1] + word[0:-1]
        print("Translation:",result)
    elif word == 'q' or word == 'Q': # notice the use of the keyword 'or'
        print("Goodbye. Have an enjoyable day.")
        break # breaks the loop, otherwise it's an 'infinite' loop
    else:
        print("Translation: " + word) # if no 'pig latin' is detected print
    