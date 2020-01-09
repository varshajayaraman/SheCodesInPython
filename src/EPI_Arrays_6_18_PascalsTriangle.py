def pascalstriangle(n):
    n-=2
    prev=[1,1]
    while n>0:
        curr = []
        for i in range(len(prev)):
            if i==0:
                curr.append(1)
                continue
            curr.append(prev[i-1]+prev[i])
        curr.append(1)
        prev=curr
        n-=1

    print(curr)
