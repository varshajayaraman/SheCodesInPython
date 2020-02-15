from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set([])
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                # print(nums[i], nums[l], nums[r])
                if nums[i] + nums[l] + nums[r] == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    # print(res)
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res
