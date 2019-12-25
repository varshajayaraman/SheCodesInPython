class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        table = []
        for i in range(len(coins)):
            res = []
            for j in range(amount + 1):
                res.append(0)
            table.append(res)

        for i in range(len(coins)):
            for j in range(amount + 1):
                if coins[i] > j:
                    if i > 0:
                        table[i][j] = table[i - 1][j]
                    continue

                else:
                    if coins[i] == j:
                        table[i][j] = 1
                    else:
                        if table[i][j - coins[i]] == 0:
                            table[i][j] = table[i - 1][j]
                        else:
                            if table[i - 1][j] != 0:
                                table[i][j] = min(table[i - 1][j], table[i][j - coins[i]] + 1)
                            else:
                                table[i][j] = table[i][j - coins[i]] + 1
        # print(table)
        if table[len(coins) - 1][amount] == 0:
            return -1
        else:
            return table[len(coins) - 1][amount]
