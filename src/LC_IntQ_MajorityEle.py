class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        can = None
        count = 0

        for n in nums:
            if count == 0:
                can = n
            if can == n:
                count += 1
            else:
                count -= 1
        return can