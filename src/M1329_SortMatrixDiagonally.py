class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        l = []
        row = len(mat)
        col = len(mat[0])
        # print(row, col)
        for j in range(col):
            l=[]
            for i in range(row):
                # print(i,j+i)
                if j+i<col:
                    l.append(mat[i][j+i])
            # print(l)
            l=sorted(l, reverse=True)
            # print(l)
            # c=j
            for i in range(row):
                if j+i<col:
                    mat[i][j+i] = l.pop()
            
         
        r=1
        while r<row-1:
            l=[]
            j=0
            for i in range(r,row): 
                if j<col:
                    l.append(mat[i][j])    
                j+=1
            l=sorted(l, reverse=True)
            j=0
            for i in range(r,row): 
                if j<col:
                    mat[i][j]=l.pop()  
                j+=1
            r+=1
            
            
        return mat
            