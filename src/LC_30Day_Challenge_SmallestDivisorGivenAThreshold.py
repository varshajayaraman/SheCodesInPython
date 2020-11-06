class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        global smallest_div
        smallest_div = math.inf
        
        def getSum(nums, div):
            # print("For div: ",div)
            res=0
            for n in nums:
                res += math.ceil(n/div)
                # print(math.ceil(n/div))
            # print("res: ",res)
            return res
        
        def bsearch(low, high, thresh):
            global smallest_div
            print(low, high)
            if low<high:
                mid = (low+high)//2
                # print(mid)
                res = getSum(nums, mid)
                if res==thresh:
                    # print("EQ", res, thresh)
                    smallest_div = mid
                    mid -=1
                    while mid>0 and res<=threshold:
                        smallest_div=mid+1
                        res = getSum(nums, mid)
                        mid -=1
                    # print("Out of EQ: ", mid)
                    
                    return smallest_div
                if res<thresh:
                    # print("LT", low, mid, high)
                    return bsearch(low, mid, thresh)
                else:
                    # print("GT", low, mid, high)
                    return bsearch(mid+1, high, thresh)
            elif low==high:
                if getSum(nums, low)<=thresh:
                    smallest_div=low
            return smallest_div
        
        def findMax(nums):
            maxVal=0
            for n in nums:
                maxVal = max(maxVal, n)
            return maxVal
        return bsearch(1,findMax(nums), threshold)