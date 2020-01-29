class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0 for x in nums]
        maxV = 0
        for i in range(len(nums)):
            if i == 0 or i == 1:
                res[i] = nums[i]

            else:
                for j in range(i - 1):
                    res[i] = max(res[i], res[j] + nums[i])

            maxV = max(maxV, res[i])

        return maxV