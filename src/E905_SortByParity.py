def sortArrayByParity(A):
    ind = -1
    for x in range(len(A)):
        if A[x]%2 == 0:
            ind += 1
            A[ind], A[x] = A[x], A[ind]
    print(A)

def swap(a,b):
    t=a
    a=b
    b=t