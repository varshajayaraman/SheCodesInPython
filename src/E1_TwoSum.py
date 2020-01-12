class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        start = 0
        end = len(nums) - 1

        for i in range(len(nums)):
            if nums[i] in numsMap.keys():
                return [numsMap[nums[i]], i]
            numsMap[target - nums[i]] = i
