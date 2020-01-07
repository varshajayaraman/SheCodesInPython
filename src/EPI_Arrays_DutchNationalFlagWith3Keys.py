def rearrange(nums):
    z,o,t=0,-1,len(nums)-1
    i=0
    while i < len(nums):
        if t<i:
            break
        if nums[i]==0:
            if o>-1:
                m=nums[z]
                nums[z]=nums[i]
                nums[i]=nums[o]
                nums[o]=m
                o+=1
            else:
                m=nums[z]
                nums[z]=nums[i]
                nums[i]=m
            z+=1
            i+=1
            continue
        if nums[i]==1:
            if o==-1:
                o=z
            m = nums[o]
            nums[o] = nums[i]
            nums[i] = m
            o += 1
            i+=1
            continue
        if nums[i]==2:
            m=nums[i]
            nums[i]=nums[t]
            nums[t]=m
            t-=1

    print(nums)