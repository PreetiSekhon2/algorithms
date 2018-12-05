from timekeeper import calcTime

def selectionSort(sampleArr):
    for i in range(0,len(sampleArr)-1):
        minpos = i
        for j in range(i+1,len(sampleArr)):
            if sampleArr[minpos] > sampleArr[j]:
                minpos = j
        temp = sampleArr[i]
        sampleArr[i] = sampleArr[minpos]
        sampleArr[minpos] = temp
    #print(sampleArr)
    return sampleArr

if __name__ == '__main__':
    arrSizes = list(range(5000,100000,10000))
    #arrSizes = [5,20,40]
    repetitions = 2

    for size in arrSizes:
        codeToSetup = '''
import time, timeit, random
from selectionsort import selectionSort
testArr = random.sample(range(1, 100000), {})
'''.format(size)
        print("Now running selectionSort with {}".format(size))
        codeToRun = '''
selectionSort(testArr)
'''
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/selectionSort.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("selectionSort()",size,res))
            myfile.close()
