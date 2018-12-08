#!/Users/preetiudas/.pyenv/shims/python3.7


from timekeeper import calcTime

def zeroesandones(sampleArr):
    testHash = {}
    oneEncountered = False
    for i in range(0,len(sampleArr)):
        if sampleArr[i] == 1 and oneEncountered == False:
            onePos = i
            oneEncountered = True
        elif sampleArr[i] == 0 and oneEncountered == True:
            sampleArr[onePos] = 0
            sampleArr[i] = 1
            onePos += 1
    #print("resultarr")
    print(sampleArr)
    return sampleArr

if __name__ == '__main__':
    arrSizes = list(range(5000,100000,10000))
    #arrSizes = [5,20,40]
    repetitions = 2

    for size in arrSizes:
        codeToSetup = '''
import random
from zeroesandones import zeroesandones
testArr = random.choices([0,1],k={})
'''.format(size)
        print("Now running zeroesandones with {}".format(size))
        codeToRun = '''
zeroesandones(testArr)
'''
        res = calcTime(codeToRun, codeToSetup,repetitions)
        with open('''timekeeper/resultfiles/zeroesandones.csv''', "a") as myfile:
            myfile.write("{},     {},     {}\n".format("zeroesandones()",size,res))
            myfile.close()
