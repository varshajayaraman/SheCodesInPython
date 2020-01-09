
def spiralArray(n):

    dir='R'
    cLength=1 #n
    res=[]
    if n==0:
        return res
    x=0
    y=0
    currStretch=0 #Fill n numbers for curr STretch times
    res.append((x, y))
    while n>0:
        i=0
        if dir=='R':
            currStretch +=1
            while i<cLength  and n>0:
                print(dir,x+1,y,n)
                res.append((x+1,y))
                x+=1
                i+=1
                n-=1
            dir='D'
            i=0
        if currStretch == 2:
            currStretch=1
            cLength += 1
        if dir=='D':
            currStretch +=1
            while i<cLength  and n>0:
                print(dir,x,y-1, n)
                res.append((x,y-1))
                y-=1
                i+=1
                n-=1
            dir='L'
            i=0
        if currStretch == 2:
            currStretch=0
            cLength += 1
        if dir == 'L':
            currStretch += 1
            while i < cLength and n > 0:
                print(dir,x-1,y, n)
                res.append((x-1, y))
                x -= 1
                i += 1
                n -= 1
            dir='U'
            i=0
        if currStretch == 2:
            currStretch = 0
            cLength += 1
        if dir == 'U':
            currStretch += 1
            while i < cLength and n > 0:
                print(dir, x,y+1, n)
                res.append((x, y+1))
                y+= 1
                i += 1
                n -= 1
            dir='R'
            i=0
        if currStretch == 2:
            currStretch=0
            cLength += 1

    print(res)