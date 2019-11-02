def arrangeCoins(n):
    i=1;
    while(n>0):
        if(n>=i):
            n-=i;
            i+=1;
        else:
            break
    print(i-1)
    return i-1;