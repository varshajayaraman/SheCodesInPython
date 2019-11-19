class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def answer(nums, start, res):
            # print(res)
            if start < len(nums):
                temp = []
                for x in res:
                    temp.append(x + [nums[start]])
                print(res, temp)
                res.extend(temp)
                answer(nums, start + 1, res)
            return res

        res = [[]]
        return (answer(nums, 0, res))