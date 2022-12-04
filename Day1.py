# Day 1

calories = input("Enter calories array")

caloryGroups = calories.split("  ")
maxResult = 0
for caloryGroup in caloryGroups :
    tempSum = sum(map(int,caloryGroup.split(" ")))
    maxResult = max(tempSum, maxResult)

print("MaxResult" + str(maxResult))
