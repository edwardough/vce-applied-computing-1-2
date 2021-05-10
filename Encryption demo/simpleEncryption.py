def simpleEncrypt( plainText, key ):
    columns = [''] * key
    chPos = 0
    textLength = len(plainText)
    while chPos < textLength:
        for i in range(key):
            if chPos < textLength:
                columns[i] = columns[i] + plainText[chPos]
                chPos += 1
            else:
                columns[i] += ''
    cipherText = ''
    for strs in columns:
        cipherText += strs
    return cipherText

def simpleDecrypt( cipherText, key ):
    pass

choice = input("[C]reate secure text file or [R]ead text file: ")
if choice.lower() == 'c':
    fname = input("Enter the file name only: ")
    plainText = input("Enter the text to store:\n")
    # TO DO: Wrap this in a try except
    key = int(input("Enter a numeric key to use: "))
    cipherText = simpleEncrypt( plainText, key )
    newFile = open(fname+".txt","w")
    newFile.write(cipherText)
    newFile.close()
elif choice == 'r':
    fname = input("Enter the file name only: ")
    key = int(input("Enter the numeric key to access the file: "))
    readFile = open(fname+".txt","r")
    cipherText = readFile.read()
    plainText = simpleDecrypt( cipherText, key )
    print(plainText)

        