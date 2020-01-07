def rearrange(nums, pi):
    min, lar=0,len(nums)-1
    tar = nums[pi]
    i=0
    while(i<len(nums)):
        print(i, min, lar)
        if lar>i:
            if nums[i]<tar:
                t=nums[min]
                nums[min]=nums[i]
                nums[i]=t
                min+=1
                i+=1
                continue
            if nums[i]==tar:
                    i+=1
                    continue
            if nums[i]>tar:
                t=nums[i]
                nums[i] = nums[lar]
                nums[lar]=t
                lar -= 1
                i-=1
                print(i)
        else:
            break
    print(nums)

