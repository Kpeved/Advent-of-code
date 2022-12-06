# Day4
inputArray = open("InputDay4.txt").read()

pairs = inputArray.split("\n")
counter = 0
for pair in pairs:
    print(pair)
    (range1, range2) = pair.split(",")
    
    (start1, end1) = range1.split("-")
    (start2, end2) = range2.split("-")
    start1 = int(start1)
    start2 = int(start2)
    end1 = int(end1)
    end2 = int(end2)
    if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1) :
        counter +=1
        

print(counter)

