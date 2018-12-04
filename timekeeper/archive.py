def calcTime(functionName, testArr):
    print (testArr)
    t1 = time.time_ns()
    functionName(testArr)
    t2 = time.time_ns()
    print (" %s takes %f" %(functionName ,(t2-t1)))
    return t2-t1

def calcPythonTime(functionName, testArr):
    print ("starting timer")
    #t = timeit.timeit(stmt = "{}({})".format(functionName, testArr), setup = "print('starting')",number = 10)
    t = timeit.repeat(stmt = "%s"%(functionName(testArr)), setup = "print('starting')",number = 10000, repeat = 10)
    print (" %s takes : " %functionName )
    print (t)
    return t
