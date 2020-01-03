def sol(nums):
    nums = sorted(nums)
    c=0
    t=nums[0]
    prev=0
    for x in range(1, len(nums)):
        if nums[x]==t:
            continue
        elif nums[x]==nums[x-1]:
            c+=prev
            print("Equal values ", x, prev, c)
        else:
            c += 1+prev
            prev=1+prev
            print("Unequal values ", x, prev, c)
    print(c)