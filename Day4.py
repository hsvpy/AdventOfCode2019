min = 356261
max = 846303
count = 0

def FindPass():
    currNum = min
    currString = str(currNum)

    while currNum < max:
        currNum += 1
        currString = str(currNum)
        if (currNum % 100000 == 0):
            digit = currString[0]
            currString = digit + digit + digit + digit + digit + digit
        if (currNum % 10000 == 0):
            digit = currString[1]
            currString = currString[0] + digit + digit + digit + digit + digit
        if (currNum % 1000 == 0):
            digit = currString[2]
            currString = currString[0] + currString[1] + digit + digit + digit + digit
        if (currNum % 100 == 0):
            digit = currString[3]
            currString = currString[0] + currString[1] + currString[2] + digit + digit + digit
        if (currNum % 10 == 0):
            digit = currString[4]
            currString = currString[0] + currString[1] + currString[2] + currString[3] + digit + digit

        currNum = int(currString)

        # Validate numbers.
        foundPair = False
        foundOddPair = False
        decreases = False
        repeat = 1
        repeatChar = '0'

        for i in range(len(currString)):
            currChar = currString[i]
            # nextChar = currString[i + 1]

            # Found a pair.
            if currChar == repeatChar:
                foundPair = True
                repeat += 1
              
            # Found an odd pair.
            if currChar != repeatChar and repeat > 2 and repeat % 2 == 1:
                foundOddPair = True
            elif currChar != repeatChar:
                repeat = 1

            # Found a decrease.
            if int(repeatChar) > int(currChar):
                decreases = True
            
            # if currChar == nextChar:
            #     foundPair = True
            #     repeat += 1
            # else:
            #     if repeat > 2 and repeat % 2 == 1:
            #         foundOddPair = True

            # if int(currChar) > int(nextChar):
            #     decreases = True

            repeatChar = currChar
            
        # Test one more time.
        if repeat > 2 and repeat % 2 == 1:
            foundOddPair = True
        
        if foundPair and foundOddPair == False and decreases == False and currNum < max:
            print(currNum)
            global count
            count += 1

FindPass()
print(count)


