class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        def flipH(A):
            for i in range(len(A)):
                m=0
                n=len(A[i])-1
                while m<n:
                    t=A[i][m]
                    A[i][m]=A[i][n]
                    A[i][n]=t
                    m+=1
                    n-=1
            return A
        def invert(A):
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j]==1:
                        A[i][j]=0
                    else:
                        A[i][j]=1
            return A
            
        A=flipH(A)
        A=invert(A)
        return A