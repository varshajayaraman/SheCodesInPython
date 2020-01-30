class Solution:
    def findMin(self, prices, maxI):
        minV = math.inf
        for i in range(maxI):
            if prices[i] < prices[maxI]:
                minV = min(minV, prices[i])
        return minV

    def maxProfit(self, prices: List[int]) -> int:
        res = [0 for x in prices]
        maxV = 0
        if len(prices) == 0:
            return 0
        minEle = prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= minEle:
                res[i] = prices[i] - minEle
            else:
                minEle = prices[i]
                res[i] = 0

            maxV = max(maxV, res[i])
        # print(res)
        return maxV