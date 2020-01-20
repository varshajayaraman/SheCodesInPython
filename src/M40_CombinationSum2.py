class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        global res
        sumVal = 0
        res = [0]

        def rec(candidates, target, sumVal, curr, ind):

            # print(sumVal, curr, ind, len(candidates))
            global res
            if sumVal > target:
                return
            if sumVal == target:
                res.append([x for x in curr])
                return

            for i in range(ind, len(candidates)):
                if i > ind and candidates[i - 1] == candidates[i]:
                    continue
                rec(candidates, target, sumVal + candidates[i], curr + [candidates[i]], i + 1)
                # rec(candidates, target, sumVal+candidates[ind], curr+[candidates[ind]], ind+1)
                # rec(candidates, target, sumVal, curr, ind+1)

        res.remove(0)
        rec(sorted(candidates), target, sumVal, [], 0)
        return res