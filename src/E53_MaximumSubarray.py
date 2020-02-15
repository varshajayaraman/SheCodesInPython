class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        currSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                currSum = max(currSum + nums[i], nums[i])
            else:
                currSum = max(currSum + nums[i], nums[i])
            maxSum = max(maxSum, currSum)
        return maxSum