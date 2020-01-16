class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def rec(ref, curr, leng, res):

            if len(curr) == leng:
                res.append([x for x in curr])
            for i in range(len(ref)):
                rec(ref[:i] + ref[i + 1:], curr + [ref[i]], leng, res)

        curr = []
        ref = nums
        rec(ref, curr, len(nums), res)
        # print("Finally: ", res)
        return res