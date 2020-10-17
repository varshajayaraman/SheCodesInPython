class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums)==0:
            return -1
        l=0
        h=len(nums)-1
        while l<=h:
            m=(l+h)//2
            
            if nums[m]==target:
                return m
            if nums[m]<target:
                if m+1==len(nums):
                    return -1
                else:
                    if nums[m+1]>target:
                        return -1
                    l=m+1
            else:
                if m==0:
                    return -1
                else:
                    if nums[m-1]<target:
                        return -1
                    h=m-1