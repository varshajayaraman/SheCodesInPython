def findPair(nums, t):
    t-=30
    hmap = {}
    si=-1
    ri=-1

    for i in range(len(nums)):
        if nums[i] in hmap.keys():
            if si==-1:
                si = hmap[nums[i]]
                ri = i
                print(si,ri)
            elif (nums[i]>nums[si] and nums[i]>nums[ri]) or (nums[hmap[nums[i]]]>nums[si] and nums[hmap[nums[i]]]>nums[ri]):
                si = hmap[nums[i]]
                ri = i
                print(si, ri)
        else:
            hmap[t-nums[i]]=i

    print("Answer", si, ri)
