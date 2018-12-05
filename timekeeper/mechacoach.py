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
    arrSizes = list(range(5000,100000,5000))
    #arrSizes = [5]#,20,40]
    repetitions = 10
    codeToSetup = '''
import random
from mechacoach import mechacoach
'''
    for size in arrSizes:
        print("Now running mechacoach with {}".format(size))
        codeToRun = '''
testArr = random.sample(range(1, 100000), {})
mechacoach(testArr)
'''.format(size)
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/mechacoach.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("mechacoach()",size,res))
            myfile.close()
