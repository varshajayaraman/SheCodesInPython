class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        global visited
        visited = set([])
        options = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

        def dfs(i, j):
            print(i, j)
            if i == destination[0] and j == destination[1]:
                return True
            visited.add((i, j))
            for k, v in options.items():
                ni = i
                nj = j

                while 0 <= (ni + v[0]) < len(maze) and 0 <= (nj + v[1]) < len(maze[0]) and maze[ni + v[0]][
                    nj + v[1]] == 0:
                    ni += v[0]
                    nj += v[1]
                if (ni, nj) not in visited:
                    if dfs(ni, nj):
                        return True

        return dfs(start[0], start[1])