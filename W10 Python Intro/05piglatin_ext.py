while True:
    words = list(input("Sentence, or 'Q' to quit > ").split(sep=" "))
    result = []
    if 'Q' in words or 'q' in words:
        break
    else:
        for word in words:   
            if word[-2:] == 'ay':
                word = word[0:-2]
                word = word[-1] + word[0:-1]
                result.append(word)
            else:
                result.append(word)
        print("Translated sentence: ",end="")
        print(" ".join(result))

    