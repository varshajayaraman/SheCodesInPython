class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        global res
        sumVal = 0
        res = [0]

        def rec(candidates, target, sumVal, curr, ind):
            print(sumVal, curr)
            global res
            if sumVal > target:
                return
            if sumVal == target:
                # print(sumVal, curr)
                if curr not in res:
                    res.append([x for x in curr])
                return

            for i in range(ind, len(candidates)):
                rec(candidates, target, sumVal + candidates[i], curr + [candidates[i]], i)
                # rec(candidates, target, sumVal+candidates[ind], curr+[candidates[ind]], ind+1)
                # rec(candidates, target, sumVal, curr, ind+1)

        res.remove(0)
        rec(candidates, target, sumVal, [], 0)
        return res