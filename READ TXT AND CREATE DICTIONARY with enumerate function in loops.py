import os
import re

regex = "[абвгдеёжзийклмнопрстуфхцчшщъьыэюя]"

path = "C:/Users/A12/Desktop/dialog/"

fileList = os.listdir(path)

print(fileList)

fileEntry = []

for file in fileList:
    currentPath = path + file
    f = open(currentPath, "rt", encoding="utf8")
    fileEntry.append(f.read())
    f.close()

resultArray = []
for txtFile in fileEntry:
    resultArray += txtFile.lower()

#print(resultArray)

output = []
for letter in resultArray:
    if re.match(regex, letter):
        output.append(letter)
    else:
        output.append(' ')

outputString = ""

for letter in output:
    outputString += letter

wordArray = outputString.split(' ')

dictionary = set(wordArray)

dictionary = list(dictionary)

dictionary.sort()


for wordIndex, word in enumerate(dictionary):
    checkLetter = 0
    wrongLetter = 0
    for i, letter in enumerate(word):
        try:
            if dictionary[wordIndex][i] == dictionary[wordIndex + 1][i]:
                checkLetter += 1
            else:
                wrongLetter += 1
        except:
            break
    if checkLetter >= 3 and 0 <= wrongLetter <= 2:
        dictionary[wordIndex] = "checked"
    if len(dictionary[wordIndex]) <= 2:
        dictionary[wordIndex] = "checked"

try:
    while(True):
        dictionary.remove("checked")
except:
    pass

print(len(dictionary))

outputFile = open("D:/Python Dictionary.txt", "w")
outputFile.write(str(dictionary))
outputFile.close()



    

    

