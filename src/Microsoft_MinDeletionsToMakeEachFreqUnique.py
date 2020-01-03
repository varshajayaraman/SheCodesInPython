from collections import defaultdict
def sol(inp):
    res=defaultdict(int)
    resSet = {0}
    maxCount=0
    totCount=0
    cres=defaultdict(list)
    resSet.remove(0)
    for x in inp:
        res[x]+=1
    for k,v in res.items():
        if v not in resSet:
            resSet.add(v)
        else:
            while v>0 and v in resSet:
                v-=1
                totCount+=1
            if v==0:
                print("Not available for ", k)

            else:
                print(totCount, " deletions for ", k)
                resSet.add(v)
            maxCount += totCount
            totCount=0
    print(maxCount)
