class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r=0
        row = len(matrix)
        if row==0:
            return []
        c=0
        col = len(matrix[0])
        res = []
        while(1):
                if c<col:
                    for i in range(c,col):
                        res.append(matrix[r][i])
                    r +=1
                else:
                    break

                if r<row:
                    for i in range(r,row):
                        res.append(matrix[i][col-1])
                    col-=1
                else:
                    break

                if col-1>=c:
                    for i in range(col-1, c-1, -1):
                        res.append(matrix[row-1][i])
                    row -=1
                else:
                    break

                if row-1>=r:
                    for i in range(row-1, r-1, -1):
                        res.append(matrix[i][c])
                    c+=1
                else:
                    break

        return res