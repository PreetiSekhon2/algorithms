from timekeeper import calcTime

def reverseArray(testArr):
    print(testArr)
    size = len(testArr)
    hiindex = size - 1
    its = int(size/2)
    for i in range(0, its):
        temp = testArr[hiindex]
        testArr[hiindex] = testArr[i]
        testArr[i] = temp
        hiindex -= 1
    # print ("Reversal done!")
    print(testArr)
    return testArr

if __name__ == '__main__':
    #arrSizes = list(range(5000,100000,5000))
    arrSizes = [5]#,20,40]
    repetitions = 10
    codeToSetup = '''
import time, timeit, random
from reversearray import reverseArray
'''
    for size in arrSizes:
        print("Now running reverseArray with {}".format(size))
        codeToRun = '''
testArr = random.sample(range(1, 100000), {})
reverseArray(testArr)
'''.format(size)
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/reverseArray.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("reverseArray()",size,res))
            myfile.close()
