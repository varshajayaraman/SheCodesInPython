class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        curr = []
        res = []

        def rec(n, k, res, curr, st):

            if len(curr) == k:
                res.append([x for x in curr])
            for i in range(st, n + 1):
                rec(n, k, res, curr + [i], i + 1)

        rec(n, k, res, curr, 1)
        return res