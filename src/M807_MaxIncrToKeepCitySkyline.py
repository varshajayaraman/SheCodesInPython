def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    rowMax = []
    colMax = []

    for i in range(len(grid)):
        rowMax.append(max(grid[i]))

    for j in range(len(grid[0])):
        maxE = 0
        for i in range(len(grid)):
            maxE = max(grid[i][j], maxE)
        colMax.append(maxE)

    print(rowMax, colMax)
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += min(rowMax[j], colMax[i]) - grid[i][j]
            grid[i][j] = min(rowMax[j], colMax[i])

    print(grid)
    print(total)
    return total