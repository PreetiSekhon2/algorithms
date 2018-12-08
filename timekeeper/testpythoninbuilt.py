#!/Users/preetiudas/.pyenv/shims/python3.7

from timekeeper import calcTime

if __name__ == '__main__':
    arrSizes = list(range(5000,100000,5000))
    #arrSizes = [5,20,40]
    repetitions = 2
    functiontorunstrings = ['reverse', 'sort', 'shuffle', 'last']

    for functionname in functiontorunstrings:

        codeToSetup = '''
import time, timeit, random
from random import shuffle
testArr = random.sample(range(1, 100000), {})
'''.format(size)

        for size in arrSizes:
            if (functionname == "reverse"):
                codeToRun = '''
testArr.reverse()
'''
            elif (functionname == "sort"):
                codeToRun = '''
testArr.sort()
'''
            elif (functionname == "shuffle"):
                codeToRun = '''
shuffle(testArr)
'''
            elif (functionname == "last"):
                codeToRun = '''
testArr[-1]
'''
            res = calcTime(codeToRun, codeToSetup,repetitions)
            with open("testpythoninbuilt.csv", "a") as myfile:
                myfile.write("{},     {},     {}\n".format(functionname,size,res))
                myfile.close()
