from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        global visited
        visited = set([])

        def dfs(i, j):
            global visited
            rows = len(grid)
            cols = len(grid[0])
            visited.add((i, j))
            grid[i][j] = -1
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d in dirs:
                nx = i + d[0]
                ny = j + d[1]
                if 0 <= nx and nx < rows and 0 <= ny and ny < cols and (nx, ny) not in visited and grid[nx][ny] == 1:
                    dfs(nx, ny)

        def expand():
            step = 0
            global visited
            rows = len(grid)
            cols = len(grid[0])
            new = list(visited)
            while True:
                visited = new
                new = []
                while len(visited) > 0:
                    curr = visited.pop(0)
                    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for d in dirs:
                        nx = curr[0] + d[0]
                        ny = curr[1] + d[1]
                        if 0 <= nx and nx < rows and 0 <= ny and ny < cols and (nx, ny):
                            if grid[nx][ny] == 0:
                                new.append((nx, ny))
                                grid[nx][ny] = -1
                            if grid[nx][ny] == 1:
                                return step
                step += 1

        def calldfs(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        return

        calldfs(grid)
        return expand()