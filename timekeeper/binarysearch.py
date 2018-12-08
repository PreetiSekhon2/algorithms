#!/Users/preetiudas/.pyenv/shims/python3.7

from timekeeper import calcTime

def binarysearch(sampleArr,searchNum):
    if(len(sampleArr) == 1  and (searchNum != sampleArr[0])):
        return False
    postocheck = len(sampleArr)//2
    #print(postocheck)
    if(searchNum==sampleArr[postocheck]):
        return True
    elif (searchNum < sampleArr[postocheck]):
        return binarysearch(sampleArr[0:postocheck],searchNum)
    else:
        return binarysearch(sampleArr[postocheck:],searchNum)


#print (binarysearch ([2,4,7,10,23,34,45,56,67,78,8888, 8888],8888))
# print (binarysearch ([2,4,7,23,34,45,56,67,78, 10],10))
# print (binarysearch ([2,4,7,23,34,45,56,67,78,100],10))


if __name__ == '__main__':
    arrSizes = list(range(5000,1000000,10000))
    #arrSizes = [6]
    repetitions = 2

    for size in arrSizes:
        codeToSetup = '''
import time, timeit, random
from random import randint
from binarysearch import binarysearch
testArr = random.sample(range(1, 1000000), {})
testArr.sort()
searchNum = randint(1,100000)
'''.format(size)
        print("Now running binarysearch with {}".format(size))
        codeToRun = '''
binarysearch(testArr,searchNum)
'''
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/binarysearch.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("binarysearch()",size,res))
            myfile.close()
