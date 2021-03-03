class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [None, None]
        for i in range(len(nums)):
            res = nums[i] % len(nums)
            if nums[res] > len(nums):
                a = nums[i] % len(nums)
                if a == 0:
                    result[0] = len(nums)
                else:
                    result[0] = a
            nums[res] += len(nums)
        # print(nums)

        for i in range(len(nums)):
            if result[1] is None and nums[i] <= len(nums):
                if i == 0:
                    result[1] = len(nums)
                else:
                    result[1] = i
        return result