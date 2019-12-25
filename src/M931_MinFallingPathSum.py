class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        minSum=math.inf
        def findMin(nums):
            minn=math.inf
            mini=0
            for x in range(len(nums)):
                if nums[x]<mini:
                    minn = nums[x]
                    mini = x
        row = len(A)
        if row==0:
            return 0
        col = len(A[0])
        if col==1:
            return sum(A[0])
        if row==1:
            return min(A[0])
        for i in range(1, row):
            for j in range(col):
                if j > 0 and j<col-1:
                    A[i][j] = min(A[i-1][j-1], A[i-1][j], A[i-1][j+1])+A[i][j]
                else:
                    if j<col-1:
                        A[i][j] = min(A[i-1][j], A[i-1][j+1])+A[i][j]
                    else:
                        A[i][j] = min(A[i-1][j-1], A[i-1][j])+A[i][j]
                if i == row-1:
                    print(minSum, A[i][j], i,j)
                    minSum = min(minSum, A[i][j])
        return minSum