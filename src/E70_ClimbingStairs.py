class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0 for i in range(n + 1)]
        if n == 1:
            return 1
        # if n==2:
        # res+=0
        res[1] = 1
        res[2] = 2
        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2]

        return res[n]