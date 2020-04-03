class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        minDisplaced = math.inf
        maxDisplaced = -math.inf
        l = 0
        r = 0
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i + 1] < nums[i]:
                minDisplaced = min(minDisplaced, nums[i + 1])

        # print(minDisplaced)
        for i in range(len(nums) - 1, -1, -1):
            # print(nums[i-1], nums[i])
            if i - 1 >= 0 and nums[i - 1] > nums[i]:
                maxDisplaced = max(maxDisplaced, nums[i - 1])

        # print(maxDisplaced)
        if minDisplaced == math.inf:
            return 0

        i = 0
        while i < len(nums) and nums[i] <= minDisplaced:
            i += 1
        l = i

        i = len(nums) - 1
        while i >= 0 and nums[i] >= maxDisplaced:
            # print(nums[i], maxDisplaced)
            i -= 1
        r = i
        # print(l, r)

        return r - l + 1