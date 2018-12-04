def reverseArray(testArr):      # Declare a function
    size = len(testArr)             # Get the length of the sequence
    hiindex = size - 1
    its = int(size/2)              # Number of iterations required
    for i in range(0, its):    # i is the low index pointer
        temp = testArr[hiindex]     # Perform a classic swap
        testArr[hiindex] = testArr[i]
        testArr[i] = temp
        hiindex -= 1            # Decrement the high index pointer
    # print ("Reversal done!")
    # print(testArr)
    return testArr
