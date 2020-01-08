def addBits(A, B):
    print(A,B)
    carry=0
    res=""
    i=2
    while i>=0:
        print(carry)
        if i==2:
            if A[i]=='1' and B[i]=='1':
                carry=1
                res = "0"+res
                i-=1
            else:
                res= str(int(A[i]) or int(B[i]))+res
                i-=1
        else:
            if carry==1:
                if (A[i]=='1' and B[i]=='1') or (A[i]=='0' and B[i]=='0'):
                    print("Here for ", i)
                    res="1"+res

                    if A[i]=='0' and B[i]=='0':
                        print("Here for ",i)
                        carry=0
                    i -= 1
                else:
                    res="0"+res
                    i-=1
            else:
                if A[i]=='1' and B[i]=='1':
                    res = "0"+res
                    carry=1
                    i-=1
                elif A[i]=='0' and B[i]=='0':
                    res = "0"+res
                    i-=1
                else:
                    res = "1"+res
                    i-=1
    if carry==1:
        res = "1"+res
        print(res)
    else:
        print(res)
