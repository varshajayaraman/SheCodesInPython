class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        minI = -1
        minGI = -1
        if len(nums) == 1:
            return

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break

        if i == 0 and nums[i] >= nums[i + 1]:
            l = 0
            h = len(nums) - 1
            while l < h:
                # print(l,h)
                t = nums[l]
                nums[l] = nums[h]
                nums[h] = t
                # print(nums)
                l += 1
                h -= 1
            return

        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                break

        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t

        l = i + 1
        h = len(nums) - 1
        while l < h:
            t = nums[l]
            nums[l] = nums[h]
            nums[h] = t
            l += 1
            h -= 1



