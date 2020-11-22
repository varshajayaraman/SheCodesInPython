class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        for i in range(0, len(nums), 2):
            even+=nums[i]
        for i in range(1, len(nums), 2):
            odd+=nums[i]
        # print(even, odd)
        pe,po = 0,0
        ways = 0
        for i in range(len(nums)-1, -1, -1):
            # print(i)
            if i%2==0:
                even -= nums[i]
            else:
                odd -= nums[i]
            if (even+po) == (odd+pe):
                ways +=1
            if i%2==0:
                pe += nums[i]
            else:
                po += nums[i]    
        return ways