class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        count = 1
        nums = set(nums)
        while nums:
            num = nums.pop()
            # nums.remove(num)
            i = 1
            while num - i in nums:
                count += 1
                nums.remove(num - i)
                i += 1

            i = 1
            while num + i in nums:
                count += 1
                nums.remove(num + i)
                i += 1
            maxCount = max(maxCount, count)
            count = 1
        return maxCount