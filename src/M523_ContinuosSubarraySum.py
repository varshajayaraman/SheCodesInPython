from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        hmapCount = {0: -1}
        sumVal = 0
        count = 0

        for i in range(len(nums)):
            if k == 0:
                if i == len(nums) - 1:
                    return False
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
                continue
            sumVal = (sumVal + nums[i]) % k
            if (sumVal) in hmapCount.keys() and (i - hmapCount[sumVal]) > 1:
                return True
            if (sumVal) not in hmapCount.keys():
                hmapCount[sumVal] = i
            # print(sumVal, nums[i], hmapCount)
        return False

        # if k == 0:
        #     return any(nums[i] == 0 and nums[i + 1] == 0 for i in xrange(len(nums) - 1))
        # mods, cum_sum_mod_k = {0: -1}, 0
        # for i in range(len(nums)):
        #     print(mods)
        #     cum_sum_mod_k = (cum_sum_mod_k + nums[i]) % k
        #     print(i - mods[cum_sum_mod_k])
        #     if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
        #         return True
        #     if cum_sum_mod_k not in mods:
        #         mods[cum_sum_mod_k] = i
        # return False