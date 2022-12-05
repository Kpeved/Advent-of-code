# Day 3

aIndex = ord('a')
zIndex = ord('z')
AIndex = ord('A')
ZIndex = ord('Z')

inputArray = open("InputDay3.txt").read()
rucksacks = inputArray.split("\n")

resultSum = 0
for rucksack in rucksacks:
    index = 0
    lettersArray = [0]*53
    for ch in rucksack:
        charAsciiIndex = ord(ch)
        if charAsciiIndex >= aIndex and charAsciiIndex <= zIndex: 
            chIndex = charAsciiIndex - aIndex + 1
        elif charAsciiIndex >= AIndex and charAsciiIndex <= ZIndex: 
            chIndex = charAsciiIndex - AIndex + 27
        print(ch + " -> " + str(chIndex))
        if index < len(rucksack)/2:
            lettersArray[chIndex] = 1
        else :
            if lettersArray[chIndex] == 1 : 
                resultSum += chIndex
                break
        index += 1
        
print(str(resultSum))
