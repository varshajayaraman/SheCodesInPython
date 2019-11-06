def solution(str):
    lc,rc=0,0
    count=0
    lastChar=str[0]
    for x in str:
        if x!=lastChar:
            if lc>0 and rc>0:
                count+=1
                lc,rc=0,0
        if x=='L':
            lc += 1
            lastChar=x
        else:
            rc += 1
            lastChar=x
        if lc==rc:
            count+=1
            lc,rc=0,0
        # print(lc,rc)

    if lc>0 and rc>0:
        count+=1
    print(count)