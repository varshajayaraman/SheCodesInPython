def solution(sale):
    lsum=0
    rsum=sum(sale)-sale[0]
    for i in range(0,len(sale)):
        if lsum==rsum:
            print (i)
            break
        else:
            lsum+=sale[i]
            rsum -= sale[i+1]