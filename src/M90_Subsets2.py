class Solution:
    def rec(self, nums, curr):
        # print("in")
        global res
        for i in range(curr, len(nums)):
            # if i==0:
            #     res.add([frozenset([[]])])
            # print("o", res)
            for x in range(len(res)):

                now = res[x]
                # print(now+[str(nums[i])], res)
                if now + [str(nums[i])] not in res:
                    res.append(now + [str(nums[i])])
                # print(res)
        # print(res)
        # res.pop(0)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        global res, k
        res = [[]]
        k = 0
        nums = sorted(nums)
        # print(res)
        self.rec(nums, 0)
        return res