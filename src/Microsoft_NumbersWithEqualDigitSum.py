from collections import defaultdict
import math
def findNum(nums):
    enab = {}
    mSum=-1

    def getSum(num):
        tot=0
        while num>0:
            tot += (num%10)
            num=num//10
        return tot


    for x in nums:
        print(enab)
        s = getSum(x)
        if s not in enab.keys():
            enab[s]=x
        else:
            mSum = max(mSum, enab[s] + x)
            enab[x] = max(enab[s], x)



    print(mSum)
    return mSum
