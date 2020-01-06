import math
def sol(nums):
    res={}
    r=0
    for x in nums:
        if x not in res.keys():
            if -x in res.keys():
                r=max(r, abs(x))
            else:
                res[x]=1
    print(r)