def beautifulArray(N):
    l=1
    h=N
    lis=[]
    while l<=h:
        lis.append(l)
        l+=1
        lis.append(h)
        h-=1
    print(lis)