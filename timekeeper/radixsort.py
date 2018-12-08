#!/Users/preetiudas/.pyenv/shims/python3.7
from timekeeper import calcTime
import numpy as np

def radixSort(sampleArr, maxLen):
    maxLen -= 1
    if maxLen == -1:
        print(sampleArr)
        return sampleArr
    for i in range(0,len(sampleArr)):
        sampleArr[i] = str(sampleArr[i]).zfill(maxLen+1)
    sampleArr = populateSubarrays(sampleArr,maxLen)
    sampleArr = radixSort(sampleArr,maxLen)

def populateSubarrays(sampleArr, postocheck):
    arr_0,arr_1,arr_2,arr_3,arr_4,arr_5,arr_6,arr_7,arr_8,arr_9 = [],[],[],[],[],[],[],[],[],[]
    for k in range(0, len(sampleArr)):
        if ((sampleArr[k] == None) or (sampleArr[k][postocheck] == None)):
            continue
        elif (sampleArr[k][postocheck]) == '0':
            arr_0.append(sampleArr[k])
        elif (sampleArr[k][postocheck]) == '1':
            arr_1.append(sampleArr[k])
        elif (sampleArr[k][postocheck]) == '2':
            arr_2.append(sampleArr[k])
        elif (sampleArr[k][postocheck]) == '3':
            arr_3.append(sampleArr[k])
        elif (sampleArr[k][postocheck]) == '4':
            arr_4.append(sampleArr[k])
        elif (sampleArr[k][postocheck]) == '5':
            arr_5.append(sampleArr[k])
        elif (sampleArr[k][postocheck]) == '6':
            arr_6.append(sampleArr[k])
        elif (sampleArr[k][postocheck]) == '7':
            arr_7.append(sampleArr[k])
        elif (sampleArr[k][postocheck]) == '8':
            arr_8.append(sampleArr[k])
        elif (sampleArr[k][postocheck]) == '9':
            arr_9.append(sampleArr[k])
    return np.concatenate([arr_0,arr_1,arr_2,arr_3,arr_4,arr_5,arr_6,arr_7,arr_8,arr_9]).ravel().tolist()


if __name__ == '__main__':
    arrSizes = list(range(5000,100000,10000))
    #arrSizes = [500]
    repetitions = 2

    for size in arrSizes:
        codeToSetup = '''
import time, timeit, random
from radixsort import radixSort
testArr = random.sample(range(1, 100000), {})
maxLen = len(str(max(testArr)))
'''.format(size)
        print("Now running radixSort with {}".format(size))
        codeToRun = '''
radixSort(testArr,maxLen)
'''
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/radixSort.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("radixSort()",size,res))
            myfile.close()
