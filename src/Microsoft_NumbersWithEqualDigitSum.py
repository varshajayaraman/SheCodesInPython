from collections import defaultdict
import math
def findNum(nums):
    enab = defaultdict(list)
    mSum=-math.inf
    def equalSum(l, mSum):
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                mSum=max(mSum, l[i]+l[j])
        return mSum
    def getSum(num):
        tot=0
        while num>0:
            tot += (num%10)
            num=num//10
        return tot
    for x in nums:
        s = getSum(x)
        enab[s].append(x)

    for k,v in enab.items():
        if len(v)<=1:
            continue
        else:
            mSum=equalSum(v, mSum)
    if mSum == -math.inf:
        print(-1)
    else:
        print(mSum)
    return
