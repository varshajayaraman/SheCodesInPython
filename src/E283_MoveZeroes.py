class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zInd=-1
        for i in range(len(nums)):
            if nums[i]==0:
                if zInd<0:
                    zInd =i
                else:
                    continue
            if nums[i]!=0:
                if zInd<0:
                    continue
                else:
                    nums[zInd]=nums[i]
                    nums[i]=0
                    zInd +=1
        return nums