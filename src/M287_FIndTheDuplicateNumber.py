class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = 0
        f = 0

        while nums[s] != nums[nums[f]]:
            s = nums[s]
            f = nums[nums[f]]

        f = nums[nums[f]]

        s = 0
        while s != f:
            s = nums[s]
            f = nums[f]
        # print(f)
        return f