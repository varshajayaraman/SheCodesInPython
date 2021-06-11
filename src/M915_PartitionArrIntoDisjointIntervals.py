class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        min_right = [0 for i in nums]
        minNum = nums[-1]
        maxNum = nums[0]
        for i in range(len(nums) - 1, -1, -1):
            minNum = min(minNum, nums[i])
            min_right[i] = minNum

        for i in range(len(nums) - 1):
            maxNum = max(maxNum, nums[i])
            if maxNum <= min_right[i + 1]:
                return i + 1
        return 0