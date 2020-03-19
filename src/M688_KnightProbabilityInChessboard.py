import numpy as np


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        global ans, direc
        ans = float(0)
        direc = [(2, 1), (1, 2), (-2, 1), (-1, 2), (-2, -1), (-1, -2), (2, -1), (1, -2)]
        dp = [[0 for i in range(N)] for j in range(N)]
        dp[r][c] = 1

        def rec(N, r, c, moves, K, val):
            global ans, direc
            if moves == K:
                ans += val
                return

            for d in direc:
                if r + d[0] < N and r + d[0] >= 0 and c + d[1] < N and c + d[1] >= 0:
                    rec(N, r + d[0], c + d[1], moves + 1, K, val / 8)

        # rec(N,r,c,0,K,1)

        for t in range(K):
            dp2 = [[0 for i in range(N)] for j in range(N)]

            for r in range(N):
                for c in range(N):
                    for d in direc:
                        if r + d[0] < N and r + d[0] >= 0 and c + d[1] < N and c + d[1] >= 0:
                            dp2[r + d[0]][c + d[1]] += dp[r][c] / 8
            dp = dp2
        return np.sum(dp)