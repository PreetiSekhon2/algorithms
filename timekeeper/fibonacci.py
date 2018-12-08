#!/Users/preetiudas/.pyenv/shims/python3.7

from timekeeper import calcTime

def fibonacci(limit):
    resArr = [0,1]
    for i in range(2,limit):
        resArr.append(resArr[i-1] + resArr[i-2])
    #print(resArr)
    return resArr

if __name__ == '__main__':
    arrSizes = list(range(5,1000000,5))
    #arrSizes = [10,20]
    repetitions = 1

    for size in arrSizes:
        codeToSetup = '''
import time, timeit, random
from fibonacci import fibonacci
'''
        print("Now running fibonacci with {}".format(size))
        codeToRun = '''
fibonacci({})
'''.format(size)
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/fibonacci3.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("fibonacci()",size,res))
            myfile.close()
