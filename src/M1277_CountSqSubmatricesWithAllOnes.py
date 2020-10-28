    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if i==0 or j==0:
                    count += matrix[i][j]
                else:
                    if matrix[i][j]==1:
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])+1
                        count += matrix[i][j]
                        
        return count