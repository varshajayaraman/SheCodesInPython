def strMatch(st):
    h=len(st)
    l=0
    res=[]
    i=0
    while(l<=h and i<len(st)):
        if st[i]=="I":
            res.append(l)
            l+=1
        else:
            res.append(h)
            h-=1
        i+=1
    if st[i-1]=="I":
        res.append(h)
    else:
        res.append(l)
    print(res)