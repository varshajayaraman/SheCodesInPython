class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxProd = nums[0]
        minProd = nums[0]
        res = maxProd

        for i in range(1, len(nums)):
            temp_maxProd = maxProd
            temp_minProd = minProd
            tmaxProd = max(nums[i], maxProd * nums[i], minProd * nums[i])
            minProd = min(nums[i], maxProd * nums[i], minProd * nums[i])
            maxProd = tmaxProd
            res = max(maxProd, res)
            # print(maxProd, minProd, res)
        # print(res)
        return res