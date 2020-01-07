def add(nums):
    cFlag=False
    carry=0
    i=len(nums)-1
    while i>=0:
        if i == len(nums)-1:
            carry = (nums[i]+1)//10
            print((nums[i]+1)%10)
            nums[i]=(nums[i]+1)%10
            i-=1
            if carry==1:
                cFlag=True
            else:
                break
        else:
            if carry==1:
                carry = (nums[i] + 1) // 10
                nums[i] = (nums[i] + 1) % 10
                if carry==0:
                    break
            i-=1
    if carry==1:
        print([1]+nums)
    else:
        print(nums)
