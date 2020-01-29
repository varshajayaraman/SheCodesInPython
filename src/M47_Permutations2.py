class Solution:
    def rec(self, nums, curr, path):
        global res
        if len(nums) == 0:
            if path not in res:
                res.append(path)
        for i in range(len(nums)):
            self.rec(nums[:i] + nums[i + 1:], curr + 1, path + [nums[i]])

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        global res
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.rec(nums[:i] + nums[i + 1:], 0, [nums[i]])
        return res