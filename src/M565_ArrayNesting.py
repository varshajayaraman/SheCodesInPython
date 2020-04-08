class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        global visited, maxLen
        visited = set()
        maxLen = 0

        def rec(nums, curr, currLen):
            global visited, maxLen

            visited.add(curr)
            if nums[curr] in visited:
                maxLen = max(maxLen, currLen)
                return
            rec(nums, nums[curr], currLen + 1)

        for n in nums:
            if n not in visited:
                rec(nums, n, 1)

        return maxLen

