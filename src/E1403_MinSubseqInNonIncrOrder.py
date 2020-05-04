class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:

        nums.sort(reverse=True)

        tot = sum(nums)

        int_sum = 0
        for i in range(len(nums)):
            int_sum += nums[i]
            tot -= nums[i]
            if int_sum > tot:
                return nums[:i + 1]

        return nums[:i]
