class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, st, e):
            while st < e:
                t = nums[st]
                nums[st] = nums[e]
                nums[e] = t
                st += 1
                e -= 1

            return nums

        if len(nums) == 0 or len(nums) == 1 or k == 0:
            return nums

        nums = reverse(nums, 0, len(nums) - 1)
        ind = k % len(nums)
        nums = reverse(nums, 0, ind - 1)
        nums = reverse(nums, ind, len(nums) - 1)

        return nums