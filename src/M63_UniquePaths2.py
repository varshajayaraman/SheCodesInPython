class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r=len(obstacleGrid)
        if r==0:
            return 0
        c=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        if obstacleGrid[r-1][c-1]==1:
            return 0
        obstacleGrid[0][0]=-1
        for i in range(r):
            for j in range(c):
                if obstacleGrid[i][j]==1 or (i==0 and j==0) :
                    continue
                if i==0:
                    obstacleGrid[i][j]=obstacleGrid[i][j-1]
                elif j==0:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]
                else:
                    if obstacleGrid[i-1][j]==1 and obstacleGrid[i][j-1]==1:
                        obstacleGrid[i][j]=1
                    else:
                        if obstacleGrid[i-1][j]==1:
                            obstacleGrid[i][j]=obstacleGrid[i][j-1]
                        elif obstacleGrid[i][j-1]==1:
                            obstacleGrid[i][j]=obstacleGrid[i-1][j]
                        else:
                            obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        print(obstacleGrid)
        if obstacleGrid[r-1][c-1]==1:
            return 0
        return -obstacleGrid[r-1][c-1]