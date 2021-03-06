#!/Users/preetiudas/.pyenv/shims/python3.7

import time, timeit, random

def subsequencesum(sampleArr, targetSum):
    testHash = {}
    for i in range(0,len(sampleArr)):
        sum = 0
        for j in range(i,len(sampleArr)):
            sum += sampleArr[j]
            if sum == targetSum:
                return True
            elif sum > targetSum:
                break
    return False

def calcTime(codeToRun, codeToSetup, repeat):
    res = timeit.repeat(stmt = codeToRun, setup = codeToSetup, number = 1, repeat = repeat)
    sum = 0
    for x in res:
        sum = sum + x
    x = sum / repeat
    return x

if __name__ == '__main__':
    arrSizes = list(range(5000,100000,10000))
    #arrSizes = [5,20,40]
    repetitions = 10

    for size in arrSizes:
        codeToSetup = '''
import time, timeit, random
from random import randint
from subsequencesum import subsequencesum
testArr = random.sample(range(1, 100000), {})
testSum = randint(1,1000)
'''.format(size)
        print("Now running subsequencesum with {}".format(size))
        codeToRun = '''

subsequencesum(testArr,testSum)
'''
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/subsequencesum.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("subsequencesum()",size,res))
            myfile.close()
