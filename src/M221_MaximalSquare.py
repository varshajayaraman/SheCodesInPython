class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=matrix
        maxv=-math.inf
        if len(matrix)==0:
            return 0
        if len(matrix)==1:
            if "1" in matrix[0]:
                return 1
            else:
                return 0
        if "1" in matrix[0]:
            maxv=1
        else:
            for j in range(len(matrix)):
                if matrix[j][0]=="1":
                    maxv=1
                    break
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if dp[i][j]=="1":
                    dp[i][j] = int(min(int(dp[i][j-1]), int(dp[i-1][j-1]), int(dp[i-1][j])))+1
                    maxv=max(maxv, dp[i][j])
        # print(dp)
        print(maxv)
        if maxv==-math.inf:
            maxv=0
        return maxv*maxv