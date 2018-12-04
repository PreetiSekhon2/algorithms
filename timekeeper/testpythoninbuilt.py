from timekeeper import calcTime

if __name__ == '__main__':
    arrSizes = list(range(5000,100000,5000))
    #arrSizes = [5,20,40]
    repetitions = 10
    functiontorunstrings = ['reverse', 'sort', 'shuffle', 'last']
    codeToSetup = '''
import time, timeit, random
from random import shuffle
'''
    for functionname in functiontorunstrings:

        for size in arrSizes:
            if (functionname == "reverse"):
                codeToRun = '''
testArr = random.sample(range(1, 100000), {})
testArr.reverse()
'''.format(size)
            elif (functionname == "sort"):
                codeToRun = '''
testArr = random.sample(range(1, 100000), {})
testArr.sort()
'''.format(size)
            elif (functionname == "shuffle"):
                codeToRun = '''
testArr = random.sample(range(1, 100000), {})
shuffle(testArr)
'''.format(size)
            elif (functionname == "last"):
                codeToRun = '''
testArr = random.sample(range(1, 100000), {})
testArr[-1]
'''.format(size)
            res = calcTime(codeToRun, codeToSetup,repetitions)
            with open("testpythoninbuilt.csv", "a") as myfile:
                myfile.write("{},     {},     {}\n".format(functionname,size,res))
                myfile.close()
