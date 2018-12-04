import time, timeit
# from addarray import addArray

def calcTime(functiontorun, arrSize, repeat):
    codeToRun = '''
testArr = random.sample(range(1, 100000), {})
{}
'''.format(arrSize, functiontorun)

    codeToSetup = '''
import time, timeit, random
from random import shuffle
'''
    t = timeit.repeat(stmt = codeToRun, setup = codeToSetup, number = 10, repeat = repeat)
    return t

if __name__ == '__main__':
    arrSizes = list(range(5000,100000,5000))
    #arrSizes = [5]
    functiontorunstrings = ['testArr.reverse()', 'testArr.sort()', 'shuffle(testArr)', 'testArr[-1]']
    for functionname in functiontorunstrings:
        repetitions = 10
        for size in arrSizes:
            res = calcTime(functionname,size,repetitions)
            sum = 0
            for x in res:
                sum = sum + x
            x = sum / repetitions
            with open("test2.csv", "a") as myfile:
                myfile.write("{},     {},     {}\n".format(functionname,size,x))
                myfile.close()
