def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def func(nums):
            sumList = []
            maxVal = 0
            for i in range(len(nums)):
                if i==0 or i==1:
                    maxVal = max(maxVal, nums[i])
                    sumList.append(maxVal)

                else:
                    maxVal = max(maxVal, nums[i]+sumList[-2])
                    sumList.append(maxVal)
            return maxVal
    
        return max(func(nums[:-1]), func(nums[1:]))