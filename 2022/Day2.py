# Day 2
# 

def mapHandToNumber(hand):
    if hand == "A" or hand == "X" : return 0
    if hand == "B" or hand == "Y" : return 1
    if hand == "C" or hand == "Z" : return 2

def compareHands(hand1, hand2):
    if hand1 == hand2 : return 3
    elif hand2 - hand1 == 1 or hand2+3 - hand1 == 1 : return 6
    else : return 0

inputArray = open("inputDay2.txt").read()

games = inputArray.split("\n")
resultScore = 0
for game in games :
    hands = game.split(" ")
    hand1 = mapHandToNumber(hands[0])
    hand2 = mapHandToNumber(hands[1])
    # hand played
    resultScore += hand2+1
    print("hand1"+ str(hand1))
    print("hand2"+ str(hand2))
    print("compareHands"+ str(compareHands(hand1, hand2)))
    resultScore += compareHands(hand1, hand2)
    

print(resultScore)



# Part 2

def mapHandToNumber(hand):
    if hand == "A" : return 0
    if hand == "B" : return 1
    if hand == "C" : return 2

def gameResult(hand2):
    if hand2 == "X" : return 0
    if hand2 == "Y" : return 3
    if hand2 == "Z" : return 6

def secondHandShouldBe(hand1, gameResult):
    if gameResult == 3 : return hand1
    elif gameResult == 0 : return (hand1+2)%3
    else : return (hand1+1)%3

inputArray = open("inputDay2.txt").read()

games = inputArray.split("\n")
resultScore = 0
for game in games :
    hands = game.split(" ")
    hand1 = mapHandToNumber(hands[0])
    gameResultParam = gameResult(hands[1])
    # game result
    resultScore += gameResultParam
    resultScore += secondHandShouldBe(hand1,gameResultParam) + 1

print(resultScore)
