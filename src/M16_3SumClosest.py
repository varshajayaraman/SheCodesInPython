class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        res = math.inf
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            tot = 0

            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if abs(target - tot) < abs(res - target):
                    # print(j,k,res, tot)
                    res = tot
                    # print(res)

                if tot == target:
                    return tot

                if tot < target:
                    j += 1
                else:
                    k -= 1

        return res

