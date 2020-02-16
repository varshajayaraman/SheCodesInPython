class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = set()
        currLength = len(res)
        minutes = 0

        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        neigh = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    res.add((i, j))
                    # break

        while currLength != len(res):
            print(res, minutes)

            currLength = len(res)
            newRes = [i for i in res]
            i = 0
            for i in newRes:
                x = i[0]
                y = i[1]

                for n in neigh:
                    new_x = x + n[0]
                    new_y = y + n[1]
                    if new_x >= 0 and new_x < row and new_y >= 0 and new_y < col:
                        if grid[new_x][new_y] == 1:
                            res.add((new_x, new_y))
            if currLength != len(res):
                minutes += 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0 and (i, j) not in res:
                    return -1
        return minutes