class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # for i in range(len(nums)-1):
        #     if nums[i]>nums[i+1]:
        #         return i
        # return len(nums)-1
        def rec(l, r):

            if l == r:
                return l
            if l < r:
                m = (l + r) // 2
                if nums[m] > nums[m + 1]:
                    return rec(l, m)
                return rec(m + 1, r)

        return rec(0, len(nums) - 1)