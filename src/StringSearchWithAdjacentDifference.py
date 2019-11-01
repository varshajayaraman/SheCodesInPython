import math
def strsearch(numList, key, x):
    i =0;
    while(i<len(numList)):
        if numList[i] == x:
            print(i)
            break
        else:
            if abs(numList[i]-x)>key:
                q=math.ceil(abs(numList[i]-x)/key)
                i+=q;
            else:
                i+=1;

    return 1;


