textToSave = ""

while True:
    newLine = input("Enter new line or QQQ to quit > ")
    if newLine != "QQQ":
        if textToSave != "":
            textToSave = textToSave + '\n' + newLine
        else:
            textToSave = textToSave + newLine
    else:
        break

print(textToSave)
newFile = open("Input.txt","w")
newFile.write(textToSave)
newFile.close()

    