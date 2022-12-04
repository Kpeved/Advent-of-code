# Day 1

calories = input("Enter calories array")

caloryGroups = calories.split("  ")
maxResult = 0
for caloryGroup in caloryGroups :
    tempSum = sum(map(int,caloryGroup.split(" ")))
    maxResult = max(tempSum, maxResult)

print("MaxResult" + str(maxResult))

# Part 2

calories = input("Enter calories array")

caloryGroups = calories.split("  ")
sortedResult = []
for caloryGroup in caloryGroups :
    sortedResult.append(sum(map(int,caloryGroup.split(" "))))

sortedResult.sort(reverse=True)
print("Sum of max 3 :" + str(sortedResult[0] + sortedResult[1] + sortedResult[2]))

