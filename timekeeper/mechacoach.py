#!/Users/preetiudas/.pyenv/shims/python3.7

from timekeeper import calcTime

def mechacoach(sampleArr):
    resArr = []
    for i in range(0,len(sampleArr)-1):
        for j in range (i+1, len(sampleArr)):
            resArr.append([sampleArr[i],sampleArr[j]])
    # print("resultarr")
    # print(resArr)
    return resArr

if __name__ == '__main__':
    arrSizes = list(range(5000,100000,10000))
    #arrSizes = [5]#,20,40]
    repetitions = 1

    for size in arrSizes:
        codeToSetup = '''
import random
from mechacoach import mechacoach
testArr = random.sample(range(1, 100000), {})
'''.format(size)
        print("Now running mechacoach with {}".format(size))
        codeToRun = '''
mechacoach(testArr)
'''
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/mechacoach.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("mechacoach()",size,res))
            myfile.close()
