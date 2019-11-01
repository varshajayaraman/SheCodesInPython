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

if __name__ == "__main__":
    strsearch([20,40,50,70,70,60], 20, 60)