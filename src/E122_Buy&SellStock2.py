class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 0:
            return 0
        b_price = prices[0]
        s_price = 0

        for x in prices[1:]:
            if x > b_price:
                profit += x - b_price
                b_price = x
            else:
                b_price = x
        return profit