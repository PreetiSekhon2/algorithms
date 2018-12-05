from timekeeper import calcTime

def bubbleSort(sampleArr):
    for i in range(0,len(sampleArr)-1):
        for j in range(i+1,len(sampleArr)):
            temp = 0
            if sampleArr[i] > sampleArr[j]:
                temp = sampleArr[i]
                sampleArr[i] = sampleArr[j]
                sampleArr[j] = temp
    #print(sampleArr)
    return sampleArr

if __name__ == '__main__':
    arrSizes = list(range(5000,100000,5000))
    #arrSizes = [5,20,40]
    repetitions = 2
    codeToSetup = '''
import time, timeit, random
from bubblesort import bubbleSort
'''
    for size in arrSizes:
        print("Now running bubblesort with {}".format(size))
        codeToRun = '''
testArr = random.sample(range(1, 100000), {})
bubbleSort(testArr)
'''.format(size)
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/bubbleSort.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("bubbleSort()",size,res))
            myfile.close()
