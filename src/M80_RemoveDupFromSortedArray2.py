class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #         i=0
        #         j=2
        #         while i<len(nums)-2:

        #             if type(nums[i])==int:
        #                 ele = nums[i]
        #             else:
        #                 ele = nums[i][0]
        #             if ele==nums[i+2]:
        #                 nums[i+2]=[nums[i+2],'a']

        #             i+=1

        #         i=0
        #         j=0
        #         while j<len(nums):
        #             if type(nums[j]) !=list:
        #                 nums[i]=nums[j]
        #                 i+=1
        #             j+=1
        #         # print(nums, i, j)
        #         return i

        i = 0
        j = 0
        while j < len(nums):
            if j < 2:
                i += 1
                j += 1
                continue
            if nums[j] != nums[i - 1] or nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i