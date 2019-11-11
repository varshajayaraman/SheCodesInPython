def stringdevoid(A,B):
    count=1
    if A>B:
        flag='A'
    else:
        flag='B'
    res=[]
    if A>0 or B>0:
        while count<3:
            if flag=='A':
                if A==0:
                    if B==0:
                        return "".join(res)
                        break
                    count=0
                    flag='B'
                    continue
                else:
                    res.append('a')
                    A-=1
                    count +=1
                    if count==3:
                        count=0
                        flag='B'

            if flag=='B':
                if B==0:
                    if A==0:
                        return "".join(res)
                        break
                    count=0
                    flag='A'
                    continue
                else:
                    res.append('b')
                    B-=1
                    count +=1
                    if count==3:
                        count=0
                        flag='A'