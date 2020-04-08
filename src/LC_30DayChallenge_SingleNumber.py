class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        l = len(nums)

        for i in range(l):
            print(nums[i], len(nums))
            e = nums[i] % l
            nums[e] += l

        for i in range(l):
            if nums[i] // l == 1:
                print(nums[i], i)
                return i