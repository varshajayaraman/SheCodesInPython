class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if type(nums[i]) != int:
        #         a = nums[i][0]
        #     else:
        #         a=nums[i]
        #     print(nums,i)
        #     if a>0 and a<=len(nums):
        #         if type(nums[a-1]) != int:
        #             continue
        #         nums[a-1] = (nums[a-1], True)
        # print(nums)
        # for i in range(len(nums)):
        #     if type(nums[i]) == int:
        #         return i+1
        # return len(nums)+1

        n = len(nums)
        nums.append(0)
        l = len(nums)
        # print(n,l)
        for i in range(n):
            if nums[i] > n or nums[i] <= 0:
                nums[i] = 0

        for i in range(n):
            # print(nums[i], nums[i]%n)
            nums[nums[i] % l] = nums[nums[i] % l] % l
            nums[nums[i] % l] += l
            # print(nums, i)

        print(nums)
        for i in range(1, len(nums)):
            if nums[i] < l:
                return i
        return len(nums)