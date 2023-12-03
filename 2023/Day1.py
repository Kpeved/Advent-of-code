----------------      # Part 1 
values = input("Enter values array")

valueLines = values.split(" ")
sum = 0
for valueLine in valueLines :
    number = 0
    for character in valueLine :
        if character.isdigit():
            number = int(character)*10
            break

    for i in range(len(valueLine) - 1, -1, -1) :
        if valueLine[i].isdigit():
            number = number + int(valueLine[i])
            break
        
    print(f"Line {valueLine} :" + str(number))
    sum = sum + number
print("Sum :" + str(sum))

-------------      # Part 2

values = input("Enter values array")

valueLines = values.split(" ")
verbalNumbers = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

sum = 0
for valueLine in valueLines :
    number = 0
    candidates = {}
    print("valueLine : " + valueLine)
    for character in valueLine :
        print("character : " + str(character))

        if character.isdigit():
            number = int(character)*10
            print("First number found : " + character)
            break
        
        new_candidates = {}
        for key,value in verbalNumbers.items() :
            if value[0] == character :
                new_candidates[key] = value[1:]
                
        for key,value in candidates.items() :
            if value[0] == character :
                new_candidates[key] = value[1:]
        
        numberFound = False
        for key, value in new_candidates.items() :
            if value == '' : 
                # numbers.append(key)
                number = key*10
                print("First number found : " + str(key))
                numberFound = True
                break
        
        if numberFound :
            break
        
        candidates = new_candidates
        print("candidates : " + str(candidates))

# Going from right to left
    candidates = {}
    print("Going from right to left")

    for i in range(len(valueLine) - 1, -1, -1) :
        character = valueLine[i]
        print("character : " + str(character))
        
        if valueLine[i].isdigit():
            number = number + int(valueLine[i])
            print("Second number found : " + valueLine[i])
            break
        
        new_candidates = {}
        for key,value in verbalNumbers.items() :
            if value[-1] == character :
                new_candidates[key] = value[:-1]
                
        for key,value in candidates.items() :
            if value[-1] == character :
                new_candidates[key] = value[:-1]
        
        numberFound = False
        for key, value in new_candidates.items() :
            if value == '' : 
                # numbers.append(key)
                number = number + key
                print("Last number found : " + str(key))
                numberFound = True
                candidates = {}
                break
        
        if numberFound :
            break
        
        candidates = new_candidates
        print("candidates : " + str(candidates))

    sum += number 
    print("sum :" + str(sum))

---------------------- Bonus -------------------------
# Convert string with written numbers into digits . This solution had bug and was fixed later

values = input("Enter values array")

valueLines = values.split(" ")
# verbalNumbers = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
verbalNumbers = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

sum = 0
for valueLine in valueLines :
    numbers = []
    number = 0
    candidates = {}
    print("valueLine : " + valueLine)
    for character in valueLine :
        print("character : " + str(character))
        print("candidates : " + str(candidates))

        if character.isdigit():
            numbers.append(int(character))
            # number = int(character)*10
            # print("First number found : " + str(number))
            # break
        
        new_candidates = {}
        for key,value in verbalNumbers.items() :
            if value[0] == character :
                new_candidates[key] = value[1:]
                
        for key,value in candidates.items() :
            if value[0] == character :
                new_candidates[key] = value[1:]
                
        for key, value in new_candidates.items() :
            if value == '' : 
                numbers.append(key)
                new_candidates.pop(key)
                break

        candidates = new_candidates
    print("numbers :" + str(numbers))
    sum = sum + numbers[0]*10 + numbers[-1]
    print("sum :" + str(sum))
