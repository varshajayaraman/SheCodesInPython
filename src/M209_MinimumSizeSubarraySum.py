class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        minLen = math.inf
        sumVal = 0
        left = 0
        for i in range(len(nums)):
            sumVal += nums[i]
            while left <= i and sumVal >= s:
                minLen = min(minLen, i + 1 - left)
                sumVal -= nums[left]
                left += 1
        if minLen == math.inf:
            return 0
        return minLen