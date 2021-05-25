class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global visited
        visited = set()
        maxArea = 0

        def dfs(grid, i, j):
            global visited
            rows = len(grid)
            cols = len(grid[0])
            visited.add((i * cols) + j)
            dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            ans = 0
            for d in dire:
                nd = (i + d[0], j + d[1])
                if nd[0] >= 0 and nd[0] < rows and nd[1] >= 0 and nd[1] < cols and grid[nd[0]][nd[1]] == 1 and (
                        (nd[0] * cols) + nd[1]) not in visited:
                    ans += dfs(grid, nd[0], nd[1])
            return ans + 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and ((i * len(grid[0])) + j) not in visited:
                    maxArea = max(maxArea, dfs(grid, i, j))
        return maxArea