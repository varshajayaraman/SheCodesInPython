import math
def search(nums, target):
    p=findPivot(nums)
    if p==-1:
        print(searchArr(nums, target, 0, len(nums)-1))
    else:
        if target == nums[p]:
            print(True)
        elif target > nums[len(nums)-1]:
            print(searchArr(nums, target, 0, p-1))
        else:
            print(searchArr(nums, target, p+1, len(nums)-1))

def searchArr(nums, target, low, high):

    if low<=high:
        mid = math.floor(low+(high-low)/2)
        print(low, mid, high, nums[mid], target)
        if nums[mid] == target:
            return True;
        else:
            if target > nums[mid]:
                return searchArr(nums, target, mid+1, high)
            else:
                return searchArr(nums, target, low, mid-1)
    return False

def findPivot(nums, low, high):
    if low<=high:
        mid = math.floor(low + (high-low)/2)
        if mid+1 < len(nums) and mid-1 >=0:
            if nums[mid]<=nums[mid+1] and nums[mid]<nums[mid-1]:
                return nums[mid]
            else:
                x=findPivot(nums, mid+1, high)
                if not x:
                 return findPivot(nums, 0, mid-1)
    # for i in range(len(nums)-1):
    #     if nums[i]>nums[i+1]:
    #         return i;
    return -1
