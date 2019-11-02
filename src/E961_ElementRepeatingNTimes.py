import math
def repeatedNTimes(A):
    d = {}
    for x in A:
        if x in d:
            d[x] +=1
        else:
            d[x]=1
    print(d)
    for x in d.keys():
        if d[x] == len(A)/2:
            print(x)
            return x;
