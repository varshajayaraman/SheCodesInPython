def arrange(a):

    ind = -1;
    i = 0;
    while(i<len(a)):
        if isEven(i):
            if a[i]>0:
                ind = find(a, max(ind,i), neg=True);
                if(ind!=-1):
                    t=a[i]
                    a[i]=a[ind]
                    a[ind]=t
                else:
                    break
        else:
            if a[i]<0:
                ind = find(a,max(ind,i), neg=False);
                if (ind != -1):
                    t = a[i]
                    a[i] = a[ind]
                    a[ind] = t
                else:
                    break;
        i+=1

    print(a)


def isEven(i):
    return i%2==0

def find(a,i,neg=True):
    flag=False
    while(i<len(a)):
        if neg:
            if a[i]<0:
                flag=True;
                break;
        else:
            if a[i]>0:
                flag = True;
                break;
        i+=1

    if(flag):
        return i;
    else:
        return -1;


