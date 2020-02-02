class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zp, tp = 0, len(nums) - 1
        op = 0
        while op <= tp:
            if nums[op] == 1:
                op += 1
            elif nums[op] == 0:
                nums[zp], nums[op] = nums[op], nums[zp]
                zp += 1
                op += 1
            else:
                nums[tp], nums[op] = nums[op], nums[tp]
                tp -= 1
        return nums



