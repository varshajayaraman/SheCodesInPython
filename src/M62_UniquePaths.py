class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1 for y in range(n)] for x in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i - 1][j] + table[i][j - 1]
        return table[m - 1][n - 1]