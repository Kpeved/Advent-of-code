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

# Part 2

aIndex = ord('a')
zIndex = ord('z')
AIndex = ord('A')
ZIndex = ord('Z')

def group_by(array, n):
    finalArray = []
    
    smallArray = []
    index = 0
    for item in array:
        if index % n == 0 and index != 0 :
            finalArray.append(smallArray)
            smallArray = []
        index += 1
        smallArray.append(item)
        
    finalArray.append(smallArray)
    return finalArray

inputArray = open("InputDay3.txt").read()
rucksacks = group_by(inputArray.split("\n"), 3)
print(rucksacks)

resultSum = 0
for rucksackGroup in rucksacks:
    
    lettersArray = [0]*53
    power = 0
    for rucksack in rucksackGroup:
        for ch in rucksack:
            charAsciiIndex = ord(ch)
            if charAsciiIndex >= aIndex and charAsciiIndex <= zIndex: 
                chIndex = charAsciiIndex - aIndex + 1
            elif charAsciiIndex >= AIndex and charAsciiIndex <= ZIndex: 
                chIndex = charAsciiIndex - AIndex + 27
            print(ch + " -> " + str(chIndex))
            lettersArray[chIndex] = lettersArray[chIndex] | pow(2, power)
            print(lettersArray) 
        power +=1
        
        j = 0
        for letter in lettersArray:
            if letter == 7 :
                resultSum += j
                break
            j += 1
    
print(str(resultSum))
