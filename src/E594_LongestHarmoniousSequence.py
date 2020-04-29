class Solution:
    def findLHS(self, nums: List[int]) -> int:

        h = {}
        maxLen = 0
        curr_len = 0
        for i in range(len(nums)):
            if h.get(nums[i]) is None:
                h[nums[i]] = [i, 1]

            else:
                occ = h[nums[i]][1]
                ind = h[nums[i]][0]
                h[nums[i]] = [ind, occ + 1]
            curr_len = h[nums[i]][1]
            if h.get(nums[i] - 1) is not None:
                # print(h, nums[i])
                curr_len += h[nums[i] - 1][1]
                maxLen = max(maxLen, curr_len)
            curr_len = h[nums[i]][1]
            if h.get(nums[i] + 1) is not None:
                curr_len += h[nums[i] + 1][1]
                maxLen = max(maxLen, curr_len)

        return maxLen