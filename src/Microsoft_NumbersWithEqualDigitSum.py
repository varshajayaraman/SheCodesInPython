from collections import defaultdict
import math
def findNum(nums):
    enab = {}
    mSum=-1


    # def equalSum(l, mSum):
    #     for i in range(len(l)):
    #         for j in range(i+1, len(l)):
    #             mSum=max(mSum, l[i]+l[j])
    #     return mSum
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
