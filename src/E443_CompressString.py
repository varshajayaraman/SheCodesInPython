import math
def compress(s):
    c=1
    j=0
    i=0
    if len(s)==1:
        return 1
    while j<len(s):
        i=j+1
        print(i,j)
        while i<len(s) and s[i] == s[j]:
           c+=1
           s.pop(i)
        if c>1:
            m=1
            while((c/10)>=1)    :
                s.insert(j+m, str((math.floor(c / 10))))
                c=c%10
                m+=1
            s.insert(j+m, str(c))
            c = 1
            j += 2
        else:
            j+=1
    if c>1:
        while (c > 0):
            print(c)
            print(c/10)
            while ((c / 10) >= 1):
                s.append(str(math.floor(c / 10)))
                c = c % 10
                m += 1
            s.append(str(c))

    print(len(s))
    print(s)