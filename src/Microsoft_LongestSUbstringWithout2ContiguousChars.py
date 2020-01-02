import math
def sol(inp):
    s,e,currSt=0,len(inp),0
    maxDiff = -math.inf
    if len(inp)<3:
        print(inp)
    for i in range(2, len(inp)):
        if inp[i]==inp[i-1]and inp[i]==inp[i-2]:
            d = (i-currSt)+1
            if d>maxDiff:
                s=currSt
                e=i
                maxDiff=d
                currSt = i-1
        print(i, len(inp), s, e)
    print(inp[s:e])