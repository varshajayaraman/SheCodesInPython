class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        hmap = {0: -1}

        maxLen = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            else:
                c -= 1

            if hmap.get(c) is None:
                hmap[c] = i
            else:
                maxLen = max(maxLen, i - hmap[c])

        return maxLen