#!/Users/preetiudas/.pyenv/shims/python3.7

from timekeeper import calcTime

def fibonacci_recursive(limit):
    if limit == 2:
        return 1
    elif limit == 1:
        return 1
    elif limit == 0:
        return  0
    else:
        return (fibonacci_recursive(limit-1)+fibonacci_recursive(limit-2))


if __name__ == '__main__':
    #arrSizes = list(range(5000,1000000,5000))
    arrSizes = list(range(5,10000,5))
    repetitions = 1

    for size in arrSizes:
        codeToSetup = '''
import time, timeit, random
from fibonacci_recursive import fibonacci_recursive
'''
        print("Now running fibonacci_recursive with {}".format(size))
        codeToRun = '''
for i in range({}):
    res = []
    res.append(fibonacci_recursive(i))
'''.format(size)
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/fibonacci_recursive.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("fibonacci_recursive()",size,res))
            myfile.close()
