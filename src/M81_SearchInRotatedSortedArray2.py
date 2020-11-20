class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        def rec(nums, l, h):
            
            if len(nums)==0 or l<0 or h<0 or l==len(nums) or h==len(nums) or l>h:
                return False
            if l==h:
                if nums[l]==target:
                    return True
                return False
            m = (l+h)//2
            print(l,m,h)
            if nums[m] == target or nums[l]==target or nums[h]==target:
                return True
            
            if target>nums[m]:
                if nums[m]==nums[h]:
                    return rec(nums, l, m-1) or rec(nums, m+1, h)
                if nums[m]>nums[h]:
                    return rec(nums, m+1, h)
                else:
                    if target<nums[h]:
                        return rec(nums, m+1, h)
                    else:
                        return rec(nums, l, m-1)
                
            else:
                if nums[m]==nums[h]:
                    return rec(nums, l, m-1) or rec(nums, m+1, h)
                if nums[m]<nums[h]:
                    print("3")
                    return rec(nums, l, m-1)
                else:
                    if target>nums[l]:
                        return rec(nums, l, m-1)
                    else:
                        return rec(nums, m+1, h)
        return rec(nums, 0, len(nums)-1)