class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = dp[i] + dp[i - c]
        return dp[-1]
