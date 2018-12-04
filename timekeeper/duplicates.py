from timekeeper import calcTime

def duplicates(sampleArr):
    testHash = {}
    for i in range(0,len(sampleArr)):
        if (sampleArr[i]) in testHash:
            testHash[sampleArr[i]] += 1
        else:
            testHash[sampleArr[i]] = 1
        keys = [key for key, value in testHash.items() if value > 1]
    return keys

if __name__ == '__main__':
    arrSizes = list(range(5000,100000,5000))
    #arrSizes = [5,20,40]
    repetitions = 10
    codeToSetup = '''
import time, timeit, random
from duplicates import duplicates
'''
    for size in arrSizes:
        print("Now running duplicates with {}".format(size))
        codeToRun = '''
testArr = random.sample(range(1, 100000), {})
duplicates(testArr)
'''.format(size)
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/duplicates.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("duplicates()",size,res))
            myfile.close()
