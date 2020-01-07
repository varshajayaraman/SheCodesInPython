def move(nums):
    ev=0
    for i in range(len(nums)):
        if nums[i]%2!=0:
          continue
        t=nums[ev]
        nums[ev]=nums[i]
        nums[i]=t
        ev+=1
    print(nums)