import math
def findDuplicates(nums):
    res=[]
    for x in nums:
        nums[x%len(nums)] += len(nums)
    # print(nums)
    for m in range(len(nums)):
        if nums[m]%len(nums) == 0:
            if math.floor(nums[m]/len(nums))>2:
                if m == 0:
                    res.append(len(nums))
                else:
                    res.append(m)
        else:
            if math.floor(nums[m]/len(nums))>1:
                print(m)
                if m==0:
                    res.append(len(nums))
                else:
                    res.append(m)
    print (res)