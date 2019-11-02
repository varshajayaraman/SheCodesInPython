def findDisappearedNumbers(nums):
    n=len(nums)
    res = []
    for i in range(n):
        print(nums[i], nums[i]%n)
        nums[nums[i]%(n)] += (n)
    for i in range(n):
        if nums[i]<=(n):
            if i==0:
                res.append(n)
                continue
            res.append(i)
    # return res
    print(nums)
    print(res)
