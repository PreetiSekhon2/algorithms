import time, timeit

def calcTime(codeToRun, codeToSetup, repeat):
    res = timeit.repeat(stmt = codeToRun, setup = codeToSetup, number = 1, repeat = repeat)
    sum = 0
    for x in res:
        sum = sum + x
    x = sum / repeat
    return x

# def calcTime(functiontorun, arrSize, repeat):
#     codeToRun = '''
# #testArr = random.sample(range(1, 100000), {})
# testArr = np.random.choice(1000, {}, replace=True)
# {}
# '''.format(arrSize, arrSize,functiontorun)
#
#     codeToSetup = '''
# import time, timeit, random
# import numpy as np
# from random import shuffle
# from duplicates import duplicates
# '''
#     t = timeit.repeat(stmt = codeToRun, setup = codeToSetup, number = 1, repeat = repeat)
#     return t
