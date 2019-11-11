import math
def sol(A, K):
        k=K
        maxele = -math.inf
        minele = math.inf
        if(len(A)==1):
            print(0)
        for i in range(0, len(A)):
            if A[i] > k:
                A[i] -= k
            else:
                A[i] += k
            if A[i] <minele:
                minele=A[i]
            if A[i]>maxele:
                maxele = A[i]
        if minele == maxele:
            print(0)
        else:
            if maxele>minele:
                print(maxele-minele)
            else:
                print(minele-maxele)