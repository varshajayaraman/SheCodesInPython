class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        global maxVal
        maxVal = 0

        def recFn(grid, i, j, row, col, currSum):
            global maxVal
            # print(j, col-1)
            if j < col:
                if grid[i][j + 1] == 0 or grid[i][j + 1] == -1:
                    # if i==2 and j==1:
                    # print("Next is not: ", i, j+1)
                    if maxVal < currSum:
                        maxVal = currSum
                    # return
                    # maxVal = max(maxVal, currSum)
                else:
                    curr = grid[i][j + 1]
                    grid[i][j + 1] = -1
                    recFn(grid, i, j + 1, row, col, currSum + curr)
                    grid[i][j + 1] = curr

            if j > 0:
                if grid[i][j - 1] == 0 or grid[i][j - 1] == -1:
                    # if i==2 and j==1:
                    # print("Next is not: ", i, j-1)
                    if maxVal < currSum:
                        maxVal = currSum
                    # return
                    # maxVal = max(maxVal, currSum)
                else:
                    curr = grid[i][j - 1]
                    grid[i][j - 1] = -1
                    recFn(grid, i, j - 1, row, col, currSum + curr)
                    grid[i][j - 1] = curr

            if i < row:
                if grid[i + 1][j] == 0 or grid[i + 1][j] == -1:
                    # if i==2 and j==1:
                    # print("Next: ", i+1, j)
                    if maxVal < currSum:
                        maxVal = currSum
                    # return
                    # maxVal = max(maxVal, currSum)
                else:
                    curr = grid[i + 1][j]
                    grid[i + 1][j] = -1
                    recFn(grid, i + 1, j, row, col, currSum + curr)
                    grid[i + 1][j] = curr

            if i > 0:
                if grid[i - 1][j] == 0 or grid[i - 1][j] == -1:
                    # if i==2 and j==1:
                    # print("Next: ", i-1, j)
                    if maxVal < currSum:
                        maxVal = currSum
                    # return
                    # maxVal = max(maxVal, currSum)
                else:
                    curr = grid[i - 1][j]
                    grid[i - 1][j] = -1
                    recFn(grid, i - 1, j, row, col, currSum + curr)
                    grid[i - 1][j] = curr

        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):

                # print(grid, "Visiting: ", i,j)
                # if i==2 and j==1:
                # print("Next: ", i, j+1)
                if grid[i][j] == 0:
                    continue
                curr = grid[i][j]
                grid[i][j] = -1
                recFn(grid, i, j, row - 1, col - 1, curr)
                grid[i][j] = curr

        # print(maxVal)
        return maxVal